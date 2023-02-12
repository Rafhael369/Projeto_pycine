# Define uma classe de modelo de tabela do SQLAlchemy para usuários
# A classe herda de Base, que é a classe base criada pelo SQLAlchemy no arquivo database/database.py
# A classe define a tabela users usando a variável de classe __tablename__
# O modelo de tabela tem quatro colunas: id, name, email, e password. Esta classe representa a tabela de usuários na base de dados e permite ao SQLAlchemy gerenciar a tabela e seus dados

from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    movie_id = Column(Integer)