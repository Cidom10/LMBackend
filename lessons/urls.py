from django.urls import path
from .views import (
    LessonList, LessonDetail,
    StepList, StepDetail,
    ComponentList, ComponentDetail,
)

urlpatterns = [
    # List view of all lessons
    path('lessons/', LessonList.as_view(), name='lesson-list'),

    # Detail view of a specific lesson
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),

    # List view of all steps for a specific lesson
    path('lessons/<int:lesson_pk>/steps/', StepList.as_view(), name='step-list'),

    # Detail view of a specific step
    path('lessons/<int:lesson_pk>/steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),

    # List view of all components for a specific step
    path('lessons/<int:lesson_pk>/steps/<int:step_pk>/components/', ComponentList.as_view(), name='component-list'),

    # Detail view of a specific component
    path('lessons/<int:lesson_pk>/steps/<int:step_pk>/components/<int:pk>/', ComponentDetail.as_view(), name='component-detail'),
]
