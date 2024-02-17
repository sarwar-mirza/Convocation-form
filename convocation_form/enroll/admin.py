from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'father_name', 'mother_name', 'date_of_birth', 'gender', 'name_of_degree', 'admission_session', 'reg_no', 'batch', 'graduating_session', 'cgpa']



