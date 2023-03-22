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