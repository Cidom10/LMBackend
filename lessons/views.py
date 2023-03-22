<<<<<<< HEAD
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
=======
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
>>>>>>> 501f00e8c5bffad53c7af67ce0a573388ba7bd50
from .models import Lesson, Step, Component
from .serializers import LessonSerializer, StepSerializer, ComponentSerializer

class LessonList(APIView):
<<<<<<< HEAD
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonDetail(APIView):
    def get_object(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    def put(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lesson = self.get_object(pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StepList(APIView):
    def get(self, request):
        steps = Step.objects.all()
        serializer = StepSerializer(steps, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StepDetail(APIView):
    def get_object(self, pk):
        try:
            return Step.objects.get(pk=pk)
        except Step.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        step = self.get_object(pk)
        serializer = StepSerializer(step)
        return Response(serializer.data)

    def put(self, request, pk):
        step = self.get_object(pk)
        serializer = StepSerializer(step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        step = self.get_object(pk)
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComponentList(APIView):
    def get(self, request):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComponentDetail(APIView):
    def get_object(self, pk):
        try:
            return Component.objects.get(pk=pk)
        except Component.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        component = self.get_object(pk)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)

    def put(self, request, pk):
        component = self.get_object(pk)
        serializer = ComponentSerializer(component, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       
=======
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
>>>>>>> 501f00e8c5bffad53c7af67ce0a573388ba7bd50
