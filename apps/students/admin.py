from django.contrib import admin
from .models import *
from apps.corecode.models import *

admin.site.register(Student)
admin.site.register(StudentBulkUpload)
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)

# Register your models here.
