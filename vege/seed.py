from faker import Faker
from .models import Department, StudentID, Student
import random

fake = Faker()

def seed_db(n=10)->None:
    try:
        departments = Department.objects.all()
        for i in range(n):
            department = random.choice(departments)
            student_id = f'STU-{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = fake.random_int(min=18, max=40)
            student_address = fake.address()

            StudentID.objects.create(student_id=student_id)
            Student.objects.create(
                department=department,
                student_id=StudentID.objects.get(student_id=student_id),
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
            
        print('Database seeded!')
    except Exception as e:
        print(e)
        print('Database seeding failed!')