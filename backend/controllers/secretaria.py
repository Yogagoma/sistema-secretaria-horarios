from sqlalchemy.orm import Session
from models.matricula import Matricula
from models.pago import Pago


def matricular_alumno(
    db: Session,
    alumno_id: int,
    curso_id: int
):

    existe = db.query(Matricula)\
        .filter(
            Matricula.alumno_id == alumno_id,
            Matricula.curso_id == curso_id
        )\
        .first()

    if existe:
        raise ValueError(
            "El alumno ya está matriculado"
        )

    matricula = Matricula(
        alumno_id=alumno_id,
        curso_id=curso_id
    )

    db.add(matricula)
    db.commit()
    db.refresh(matricula)

    return matricula


def registrar_pago(
    db: Session,
    alumno_id: int,
    monto: float
):

    pago = Pago(
        alumno_id=alumno_id,
        monto=monto
    )

    db.add(pago)
    db.commit()
    db.refresh(pago)

    return pago


def listar_matriculas(
    db: Session
):

    return db.query(Matricula).all()


def consultar_pagos_alumno(
    db: Session,
    alumno_id: int
):

    return db.query(Pago)\
        .filter(Pago.alumno_id == alumno_id)\
        .all()