import uuid

from django.core.management import BaseCommand
from faker import Faker
from home.models import Student, Subject, Book, Teacher
import random

class Command(BaseCommand):

    help = "Insert new students in the system"

    def add_arguments(self, parser):
        """This function is parsing all the arguments."""

        parser.add_argument("-l", "--len", type=int, default=10)

    def handle(self, *args, **options):
        """This function initializes Faker and
        generates information for the each field
        in the model "Student"."""
        faker = Faker()

        subjects_name = ["Python", "Java", "Math", "History"]

        for _ in range(options['len']):

            self.stdout.write('Start inserting Students')
            book = Book()
            book.title = uuid.uuid4()
            book.save()

            subject, _ = Subject.objects.get_or_create(title=random.choice(subjects_name))
            subject.save()


            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_int(min=18, max=80)
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_of_birth()
            student.email = faker.email()
            student.social_url = "https://www.instagram.com/" + student.name + student.surname
            student.save()
            student.book = book
            student.subject = subject
            student.save()


            teacher, _ = Teacher.objects.get_or_create(name=faker.name())
            teacher.students.add (student)
            teacher.save()

        self.stdout.write('End inserting Students')
