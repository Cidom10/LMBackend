from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lesson, Step, Component
from .serializers import LessonSerializer, StepSerializer, ComponentSerializer

class LessonList(APIView):
    def get(self, request, id=None):

        if id:
            data = Lesson.objects.filter(id=id)
        else:
            data = Lesson.objects.all()
        serializer = LessonSerializer(data, many=True)
        return Response(serializer.data)

class StepList(APIView):
    def get(self, request, id=None):
        
        if id:
            data = Step.objects.filter(id=id)
        else:
            data = Step.objects.all()
        serializer = StepSerializer(data, many=True)
        return Response(serializer.data)

class ComponentList(APIView):
    def get(self, request, id=None):
        if id:
            data = Component.objects.filter(id=id)
        else:
            data = Component.objects.all()
        serializer = ComponentSerializer(data, many=True)
        return Response(serializer.data)