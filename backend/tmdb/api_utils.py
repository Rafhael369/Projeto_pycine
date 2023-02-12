from service.service import Service
from tmdb.models import TMDBMovie
import requests

key = '75064829deabdc50b2d14f2810fe4267'

# A classe "RequestApi" tem métodos que fazem requisições à API do The Movie Database (TMDB) e retornam informações sobre filmes ou artistas
# A chave de API "key" é usada para autenticar as requisições
class RequestApi:
    #Criei um para retornar um filme por id, por vez
    @staticmethod
    def get_movie(movie_id):
        endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}'
        r = requests.get(endpoint)
        data = r.json()
        # print(data)
        results = data
        return results

    @staticmethod
    def test():
        print('[ok] from RequestApi')

    @staticmethod
    def get_movie_popular_by_genre(genre: int):
        endpoint = f'https://api.themoviedb.org/3/discover/movie/?api_key={key}&certification_country=US&certification=R&sort_by=vote_count.desc&with_genres={genre}'
        r = requests.get(endpoint)
        data = r.json()
        results = data['results']
        return results

    @staticmethod
    def get_artista_by_name(name):
        endpoint = f'https://api.themoviedb.org/3/search/person?api_key={key}&query={name}'
        r = requests.get(endpoint)
        data = r.json()
        results = data['results'][0]['id']
        endpoint = f'https://api.themoviedb.org/3/person/{results}?api_key={key}'
        r = requests.get(endpoint)
        data = r.json()
        results = {'id': data['id'], 'nome': data['name'], 'imagem': data['profile_path'], 'popularidade': data['popularity']}
        return results

    @staticmethod
    def get_artista(person_id):
        endpoint = f'https://api.themoviedb.org/3/person/{person_id}?api_key={key}'
        r = requests.get(endpoint)
        data = r.json()
        results = data
        return results

# A classe "MovieUtils" tem métodos que ajudam a tratar e formatar as informações retornadas pela API
class MovieUtils:
    @staticmethod
    def get_genres(genre_ids):
        genres = Service.get_genres()
        genres_names = [g['name'] for g in genres if g['id'] in genre_ids]
        return " | ".join(genres_names)

    @staticmethod
    def get_image_path(poster_path):
        return f"https://image.tmdb.org/t/p/w185{poster_path}"

    @staticmethod
    def get_movies(genre: int):
        results = RequestApi.get_movie_popular_by_genre(genre)
        movies = []
        for movie in results:
            m = TMDBMovie(
                movie['id'],
                movie['original_title'],
                genres=MovieUtils.get_genres(
                    movie['genre_ids']
                ),
                poster_path=MovieUtils.get_image_path(
                    movie['poster_path']
                )
            )
            movies.append(m)
        return movies