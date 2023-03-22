from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from .models import Lesson
from .models import Step
from .models import Component

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(Component)
>>>>>>> 501f00e8c5bffad53c7af67ce0a573388ba7bd50
