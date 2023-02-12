# 3 classes Pydantic para modelos de usuário. A classe UserModel é a classe base para todos os modelos de usuário e define três campos obrigatórios: name, password, e email
# A classe UserCreate herda de UserModel e redefine o campo password como obrigatório
# A classe User herda de UserModel e adiciona um campo obrigatório id
# A classe User tem a configuração orm_mode = True, o que significa que esta classe será usada pelo SQLAlchemy como modelo de tabela para a tabela de usuários na base de dados 
# Estas classes fornecem uma abstração para dados de usuários e são usadas para validar e mapear entre dados da aplicação e dados do banco de dados

from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    password: str
    email: str

class UserCreate(UserModel):
    password: str

class User(UserModel):
    id: int

    class Config:
        orm_mode = True
    
class FavoriteCreate(BaseModel):
    user_id: int
    movie_id: int

    class Config:
        orm_mode = True