import requests
import csv
from PIL import Image
from io import BytesIO
 
API_URL_BASE = "https://collectionapi.metmuseum.org/public/collection/v1"
NATIONALITIES_URL = "https://drive.google.com/uc?export=download&id=1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A"
 
def get_api_data(endpoint: str, params: dict = None) -> dict:
    url = f"{API_URL_BASE}/{endpoint}"
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None
 
def cargar_nacionalidades():
    try:
        response = requests.get(NATIONALITIES_URL)
        response.raise_for_status()
        content = response.content.decode('utf-8').splitlines()
        reader = csv.reader(content)
        return [row[0] for row in reader if row]
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la lista de nacionalidades: {e}")
        return []
 
def mostrar_imagen_pillow(url: str, title: str):
    print(f"Cargando imagen para '{title}'...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        imagen_bytes = BytesIO(response.content)
        img = Image.open(imagen_bytes)
        img.show(title=title)
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    except IOError as e:
        print(f"Error al abrir la imagen con Pillow: {e}")
