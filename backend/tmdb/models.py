# Classe Genre criada para representar os gêneros de filmes
# Classe TMDBMovie criada para representar os filmes
# A classe tem um método construtor __init__ que inicializa os atributos quando um novo objeto TMDBMovie é criado. 
# Os argumentos para o construtor são opcionais e têm valores padrão de None se não forem fornecidos

from enum import Enum

class Genre(Enum):
    Drama = 18
    Comedia = 35
    Scifi = 878

class TMDBMovie:
    def __init__(self, 
            id, 
            title, 
            popularity=None,
            poster_path=None,
            release_date=None,
            genres=None
        ):
        self.id = id
        self.title = title
        self.popularity = popularity
        self.poster_path = poster_path
        self.release_date = release_date
        self.genres = genres

