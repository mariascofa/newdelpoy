import re, gender_guesser.detector as gender


from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from home.models import Student

# @receiver(pre_delete, sender=Student)
# def delete_student(**kwargs):
#     """Doesn't let to delete students from a data base."""
#     raise Exception ("don't delete")

@receiver(pre_save, sender=Student)
def pre_save_sex(sender, instance,  **kwargs):
    """Identifies the gender by name of the student and puts
    the result into the field with student's gender."""
    detect = gender.Detector()
    instance.sex = detect.get_gender(instance.name)

@receiver(pre_save, sender=Student)
def pre_save_name(sender, instance, **kwargs):
    """Normalizes (removes special characters and lead to lower case)
    name and surname of the student."""
    instance.normalized_name = re.sub('[^\w\s]|_', '', instance.name + instance.surname).lower()


