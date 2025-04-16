from datetime import date, timedelta
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Group, Student, Teacher, Subject, Grade

fake = Faker()

engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=f'Group {i}') for i in range(1, 4)]
session.add_all(groups)
session.commit()


teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()


subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(6)]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()


for student in students:
    for subject in subjects:
        for _ in range(random.randint(2, 5)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.uniform(60, 100),
                date_of=fake.date_between(start_date='-1y', end_date='today')
            )
            session.add(grade)

session.commit()
session.close()
