from django.urls import path
from .views import *

urlpatterns = [
 path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('question-options/', QuestionOptionList.as_view(), name='question-option-list'),
    path('question-options/<int:pk>/', QuestionOptionDetail.as_view(), name='question-option-detail'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('steps/', StepList.as_view(), name='step-list'),
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),
    path('surveys/', SurveyList.as_view(), name='survey-list'),
    path('surveys/<int:pk>/', SurveyDetail.as_view(), name='survey-detail'),
]