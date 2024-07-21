from rest_framework import serializers
from .models import Category, QuestionOption, Question, Step, Survey

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['id', 'label', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'label', 'options', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class StepSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = ['id', 'name', 'description', 'questions', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class SurveySerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'steps', 'category', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
