from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from home.models import Student, Book, Subject, Teacher


class StudentForm(ModelForm):
    """Data base info"""

    class Meta:
        model = Student
        fields = ["name", "surname", "age", "sex", "address",
                  "description", "birthday", "email", "social_url"]


class BookForm(ModelForm):
    """Data base info"""

    class Meta:
        model = Book
        fields = ["id"]


class SubjectForm(ModelForm):
    """Data base info"""

    class Meta:
        model = Subject
        fields = ["title"]


class TeacherForm(ModelForm):
    """Data base info"""

    class Meta:
        model = Teacher
        fields = ["name"]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



