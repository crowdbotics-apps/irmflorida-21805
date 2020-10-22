from django.contrib import admin
from .models import CustomerProfile, InviteCode, Notification, TaskerProfile

admin.site.register(TaskerProfile)
admin.site.register(InviteCode)
admin.site.register(Notification)
admin.site.register(CustomerProfile)

# Register your models here.
