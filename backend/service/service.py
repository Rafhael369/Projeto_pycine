# Classe responsável por fazer a leitura do arquivo JSON e retornar os dados

import json

class Service:

    @staticmethod
    def get_genres():
        genres = json.load(open('./data/genres.json'))
        return genres
