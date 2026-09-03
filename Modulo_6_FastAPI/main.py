from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Cria as tabelas no PostgreSQL se não existir
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Estudantes
@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def criar_estudante(studant: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_student = models.Estudante(**studant.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def ler_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).all()
    return estudantes

# Matriculas
@app.post('/matriculas/', response_model=schemas.MatriculaResponse)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matriculas(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matriculas/', response_model=List[schemas.MatriculaResponse])
def ler_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matriculas).all()
    return matriculas



