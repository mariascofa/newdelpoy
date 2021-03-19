"""hmw5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from home.views import StudentView, CreateView, UpdateView, BookView, SubjectView, TeachersView, BookDeleteView, \
    SubjectUpdateView, DeleteSubjectView, TeacherUpdateView, TeacherDeleteView, AddStudentView, TeacherStudentView, \
    CurrencyView, CSVView, JsonView, SendEmailView, DeleteView, Register, ActivateView, Logout, Login

urlpatterns = [
    path('currency/', CurrencyView.as_view(), name='currency'),
    path('admin/', admin.site.urls),
    path('subjects/', SubjectView.as_view(), name='subjects'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('', StudentView.as_view(), name='students'),
    path("students/create/", CreateView.as_view(), name='create'),
    path("students/update/<pk>/", UpdateView.as_view(), name="update"),
    path("students/delete/<pk>/", DeleteView.as_view(), name="delete"),
    path("books/", BookView.as_view(), name="book"),
    path("books/delete/<id>/", BookDeleteView.as_view(), name="delete_book"),
    path("subjects/update/<id>/", SubjectUpdateView.as_view(), name="update_subject"),
    path("subjects/delete/<subject_id>/<student_id>/", DeleteSubjectView.as_view(), name="student_subject"),
    path("teachers/update/<id>/", TeacherUpdateView.as_view(), name="update_teacher"),
    path("teachers/delete/<student_id>/<teacher_id>/", TeacherDeleteView.as_view(), name="delete_teacher"),
    path("subjects/update/<subject_id>/<student_id>/", AddStudentView.as_view(), name="add_student"),
    path("register", Register.as_view(), name="register"),
    path("teacher/update/<teacher_id>/<student_id>/", TeacherStudentView.as_view(), name="teacher_student"),
    path("json/", JsonView.as_view(), name="json"),
    path("css/", CSVView.as_view(), name="css"),
    path("email/", SendEmailView.as_view(), name="email"),
    path('activate/<uid>/<token>', ActivateView.as_view(), name='activate_view'),
    path('logout', Logout.as_view(), name='logout'),
    path('login', Login.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

