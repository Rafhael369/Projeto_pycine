# Projeto Pycine - Backend

## Clonar o Projeto Pycine - Backend

```bash
cd Projeto_Pycine/backend

# CRIAR O VIRTUAL ENV:
# OPÇÃO 1 (máquina do LAB):
python3 -m venv env --without-pip --system-site-packages
# OPÇÃO 2 (máquina pessoal):
python3 -m venv env

# Ativar o ambiente virtual:
source env/bin/activate

# instalar dependências
pip install -r requirements.txt

# rodar o servidor
uvicorn main:app --reload
```

## Atualizar código do vscode com o código no git

**Atenção!!!** Esse comando apagará qualquer mudança no seu código e substituirá pelo código que está no github:

```bash
git fetch
git reset --hard origin/master
```

## Erro **ModuleNotFound**

Se ocorrer o erro "ModuleNotFound", abrir o terminal (na mesma pasta do projeto) e rodar o comando:

```bash
export PYTHONPATH=.
```

## ORM - Mapeamento Classe para Tabela

Para conversão das classes em tabelas usar o ORM sqlalchemy:
- [Configuração do SQLite](https://fastapi.tiangolo.com/tutorial/sql-databases/)

```bash
pip install sqlalchemy
```