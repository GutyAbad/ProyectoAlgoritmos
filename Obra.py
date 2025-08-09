class ObraDeArte:
 
    def __init__(self, object_id: int, title: str, artist_name: str,
                 artist_nationality: str, artist_begin_date: str,
                 artist_end_date: str, classification: str, object_date: str,
                 image_url: str):
       
        self.object_id = object_id
        self.title = title
        self.artist_name = artist_name
        self.artist_nationality = artist_nationality
        self.artist_begin_date = artist_begin_date
        self.artist_end_date = artist_end_date
        self.classification = classification
        self.object_date = object_date
        self.image_url = image_url
 
    def __str__(self):
       
        return (
            f"ID de Obra: {self.object_id}\n"
            f"Título: {self.title}\n"
            f"Artista: {self.artist_name}\n"
        )
