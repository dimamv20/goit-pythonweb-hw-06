from sqlalchemy import func, desc
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import Session

def select_1(session: Session):
    result = (
        session.query(Student, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result

def select_2(session: Session, subject_id: int):
    result = (
        session.query(Student, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )
    return result

def select_3(session: Session, subject_id: int):
    result = (
        session.query(Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return result

def select_4(session: Session):
    result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
    return result

def select_5(session: Session, teacher_id: int):
    result = (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return result

def select_6(session: Session, group_id: int):
    result = session.query(Student).filter(Student.group_id == group_id).all()
    return result

def select_7(session: Session, group_id: int, subject_id: int):
    result = (
        session.query(Student.fullname, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result

def select_8(session: Session, teacher_id: int):
    result = (
        session.query(func.round(func.avg(Grade.grade), 2))
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    return result

def select_9(session: Session, student_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )
    return result

def select_10(session: Session, student_id: int, teacher_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id,
            Grade.subject_id == Subject.id
        )
        .group_by(Subject.id)
        .all()
    )
    return result
