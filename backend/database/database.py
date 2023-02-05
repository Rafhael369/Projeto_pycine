# Configuracao do SQLAlchemy
# Cria uma engine de conexão com o banco de dados SQLite com a URL especificada em SQLALCHEMY_DATABASE_URL 
# A classe base para modelos de tabelas é criada usando declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/pycine.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()