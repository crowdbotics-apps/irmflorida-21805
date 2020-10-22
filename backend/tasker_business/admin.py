from django.contrib import admin
from .models import BusinessPhoto, TaskerAvailability, TaskerSkill, Timeslot

admin.site.register(Timeslot)
admin.site.register(TaskerAvailability)
admin.site.register(TaskerSkill)
admin.site.register(BusinessPhoto)

# Register your models here.
