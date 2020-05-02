from django.contrib import admin

# Register your models here.
from patient.models import *

admin.site.register(Department)
admin.site.register(Symptom)
admin.site.register(Doctor)
admin.site.register(Questions)
admin.site.register(Medicine)
