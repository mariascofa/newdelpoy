import django_filters

from home.models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = "book__title", "teacher__name", "subject__title"
