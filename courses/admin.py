from django.contrib import admin

# Register your models here.

from .models import Course, Step

admin.site.register(Course)
admin.site.register(Step)