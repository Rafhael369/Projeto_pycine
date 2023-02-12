# Funções que manipulam os objetos de um usuário
# As funções sao criar, obter, atualizar, excluir usuários e obter usuários por email
# Cada função recebe uma sessão do SQLAlchemy (db) e outros parâmetros específicos, como ID de usuário ou objeto usuário
# As alterações na base de dados são confirmadas usando db.commit() e o estado do objeto é atualizado usando db.refresh(db_user)

from sqlalchemy.orm import Session
import model.models as models
import database.schemas as schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def update_user(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Salva o filme favorito de um usuário no banco de dados
def save_favorite(db: Session, favorite: schemas.FavoriteCreate):
    db_favorite = models.Favorite(user_id=favorite.user_id, movie_id=favorite.movie_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

# Retorna os filmes favoritos de um usuário
def get_favorite_movies(db: Session, user_id: int):
    return db.query(models.Favorite.movie_id).filter(models.Favorite.user_id == user_id).all()