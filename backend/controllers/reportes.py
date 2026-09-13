from sqlalchemy import func
from sqlalchemy.orm import Session

from models.secretaria import Estudiante
from models.academico import Nota


def reporte_estudiantes(
    db: Session
):

    cantidad = db.query(
        func.count(Estudiante.id)
    ).scalar()

    return {
        "total_estudiantes": cantidad
    }


def reporte_promedios(
    db: Session
):

    resultados = db.query(
        Nota.estudiante_id,
        func.avg(
            Nota.calificacion
        ).label("promedio")
    )\
    .group_by(
        Nota.estudiante_id
    )\
    .all()

    return resultados


def reporte_aprobados(
    db: Session
):

    resultados = []

    promedios = reporte_promedios(db)

    for item in promedios:

        if item.promedio >= 70:

            resultados.append(
                {
                    "estudiante_id":
                    item.estudiante_id,

                    "promedio":
                    round(item.promedio, 2)
                }
            )

    return resultados