from rest_framework import generics
from .models import Category, QuestionOption, Question, Step, Survey
from .serializers import CategorySerializer, QuestionOptionSerializer, QuestionSerializer, StepSerializer, SurveySerializer

# Category Views
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# QuestionOption Views
class QuestionOptionList(generics.ListCreateAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer

class QuestionOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer

# Question Views
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Step Views
class StepList(generics.ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

# Survey Views
class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
