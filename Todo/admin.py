from django.contrib import admin
from .models import *

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_add', 'completed')


admin.site.register(Task, TaskAdmin)

