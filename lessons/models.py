from django.db import models

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=400, default="Lesson created for Cyber.org")

    def __str__(self):
        return self.title



class Step(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=None)
    stepTitle = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.stepTitle + " in " + self.lesson.title

class Component(models.Model):
    compTypes = [
        ('header',      'Header'), 
        ('section',     'Section'),
        ('blockquote',  'Blockquote'),
        ('media',       'Media'),
        ('carousel',    'Carousel'),
        ('footer',      'Footer')
    ]

    # Reference to parent Step
    step = models.ForeignKey(Step, on_delete=models.CASCADE, default=None)
    # Specifies the type of component form list above
    componentType = models.CharField(
        max_length=10,
        choices=compTypes,
        default="section"
    ),
    # Information of component (differs by component type)
    info = models.JSONField(default=dict)

    def __str__(self):
        return "Comp in " + self.step.stepTitle

# https://realpython.com/django-rest-framework-quick-start/ 