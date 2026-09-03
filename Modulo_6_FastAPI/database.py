from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv('DATABASE_URL')

# Faz a conversa entre sql e FastAPI
engine = create_engine(DATABASE_URL)
# Cria conexão temporario com banco de dados
SessionLocal = sessionmaker(bind=engine)
# Permite criar as entidades
Base = declarative_base()

