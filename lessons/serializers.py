<<<<<<< HEAD
from models import Lesson, Step, Component
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'
=======
from rest_framework import serializers

from lessons.models import Component, Lesson, Step


class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = ('title', "description")

class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('lesson', 'stepTitle')

class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component
        fields = ('componentType', "info")
>>>>>>> 501f00e8c5bffad53c7af67ce0a573388ba7bd50
