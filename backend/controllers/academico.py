from sqlalchemy.orm import Session
from models.academico import Nota


def registrar_calificacion(
    db: Session,
    estudiante_id: int,
    materia_id: int,
    calificacion: float
):
    
    if calificacion < 0 or calificacion > 100:
        raise ValueError(
            "La calificación debe estar entre 0 y 100"
        )

    nota = Nota(
        estudiante_id=estudiante_id,
        materia_id=materia_id,
        calificacion=calificacion
    )

    db.add(nota)
    db.commit()
    db.refresh(nota)

    return {
        "mensaje": "Calificación registrada correctamente"
    }


def calcular_promedio(
    db: Session,
    estudiante_id: int
):

    notas = db.query(Nota)\
        .filter(Nota.estudiante_id == estudiante_id)\
        .all()

    if len(notas) == 0:
        return {
            "promedio": 0
        }

    promedio = sum(
        nota.calificacion
        for nota in notas
    ) / len(notas)

    return {
        "promedio": round(promedio, 2)
    }


def listar_calificaciones(
    db: Session,
    estudiante_id: int
):

    return db.query(Nota)\
        .filter(
            Nota.estudiante_id == estudiante_id
        )\
        .all()