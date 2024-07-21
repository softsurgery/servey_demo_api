from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "categories"

class QuestionOption(models.Model):
    label = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "options"

class Question(models.Model):
    label = models.CharField(max_length=255)
    options = models.ManyToManyField(QuestionOption, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['created_at']

class Step(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']

class Survey(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    steps = models.ManyToManyField(Step, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "surveys"