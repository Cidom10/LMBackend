from django.contrib import admin

from .models import Lesson
from .models import Step
from .models import Component

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(Component)