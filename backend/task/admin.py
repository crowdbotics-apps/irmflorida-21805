from django.contrib import admin
from .models import Message, Rating, Task, TaskTransaction

admin.site.register(Rating)
admin.site.register(TaskTransaction)
admin.site.register(Message)
admin.site.register(Task)

# Register your models here.
