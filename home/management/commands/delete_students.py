from django.core.management import BaseCommand
from home.models import Student

class Command(BaseCommand):
    def handle(self, *args, **options):
        last_student = Student.objects.last()
        last_student.delete()



