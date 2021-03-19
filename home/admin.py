from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.utils.html import format_html, format_html_join

from home.models import Student


class StudentAdmin(ModelAdmin):
    """Displays records of the project that needs to
    be created, updated, reviewed or deleted."""

    list_display = ('email', "custom_field", 'birthday')
    readonly_fields = ("custom_field",)

    def custom_field(self, instance):
        """Joins student's name and the surname
         into one field, that work as
         a link to the student's social network page. """
        full_name = instance.name + " " + instance.surname
        if instance.social_url is None:
            return full_name
        else:
            return format_html("<a href='{url}'>{full_name}</a>", full_name=full_name,
                               url=instance.social_url)



admin.site.register(Student, StudentAdmin)
