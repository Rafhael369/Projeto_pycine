# Importação de pacotes FastAPI, CORS, dependências, exceções HTTP, Pydantic, SQLAlchemy para o desenvolvimento da API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Importar classes para persistir dados no SQLite
import database.crud as crud
import model.models as models
from database.schemas import UserModel, User, FavoriteCreate
from database.database import SessionLocal, engine
from service.service import Service

# Importar MovieUtils e Genre para uso na API do TMDB
from tmdb.models import Genre
from tmdb.api_utils import RequestApi, MovieUtils
app = FastAPI()

#CORS- Permite que o Svelte acesse o FastAPI
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Testar para verificar se o banco de dados não é apagado toda vez que o FastAPI é iniciado
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =============================
# FAVORITE (sqlite)
# =============================
# Salva o filme favorito de um usuário se ele ja nao estiver favoritado, ou seja, se ja tiver um id igual
# no banco de dados
@app.post("/favorite/create")
async def create_favorite(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    db_fav_id = crud.get_favorite_movies(db, favorite.user_id)
    for i in db_fav_id:
        if i[0] == favorite.movie_id:
            raise HTTPException(
                status_code=400,
                detail="Movie already in favorites"
            )
    db_fav = crud.save_favorite(db, favorite)
    return db_fav

# Retorna os filmes favoritos de um usuário, e monta um json simples com nome e path do poster
@app.get("/favorite/movies/{user_id}")
async def get_favorite_movies(user_id: int, db: Session = Depends(get_db)):
    id_movies = crud.get_favorite_movies(db, user_id)
    filmes = []
    for i in id_movies:
        data = RequestApi.get_movie(i[0])
        if "success" in data:
            continue
        else:
            filmes.append({"name" : data['original_title'],
                            "poster_path" : "https://image.tmdb.org/t/p/w185"+data['poster_path'],})
        
    return filmes

# =============================
# USER (sqlite)
# =============================

@app.post("/user/create")
async def create_user(user: UserModel, db: Session = Depends(get_db)):
    print(user)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    new_user = crud.create_user(db=db, user=user)
    return new_user


@app.get("/user/list")
async def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/user/delete/{id}")
async def delete_user(id=int, db: Session = Depends(get_db)):
    return crud.delete_user(db, id)

@app.post("/user/update")
def update_user(user: User, db: Session = Depends(get_db)):
    return crud.update_user(db, user)

@app.get("/user/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, id)


# =============================
# MOVIE (tmdb)
# =============================

@app.get("/genres")
async def get_genres():
    return Service.get_genres()

@app.get("/movies")
async def get_movies():
    movies = MovieUtils.get_movies(Genre.Scifi.value)
    return movies

@app.get("/artista/id/{id}")
async def get_artista(id):
    artista = RequestApi.get_artista(id)
    if "name" not in artista:
        raise HTTPException(
            status_code=404, detail="No person found with id = {id}")
    return {
        "name": artista['name'],
        "id": artista['id'],
        "popularity": artista['popularity'],
        "biography": artista['biography'],
    }


@app.get("/artist/name/{nome}")
async def get_artista(nome):
    artista = RequestApi.get_artista_by_name(nome)
    return artista


@app.get("/find/{title}/{genre}")
async def find(title: str, genre):
    import json
    data = json.load(open('filmes.json'))
    encontrou = []
    for filme in data:
        if title.lower() in filme['title'].lower():
            encontrou.append(filme)
    return encontrou


@app.get("/")
async def home():
    return {"msg": "pycine back-end"}