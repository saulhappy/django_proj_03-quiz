from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    title = models.CharField(max_length=140, default="New Quiz")
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    SCALE_CHOICES = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )

    METHOD_CHOICES = (
        (0, 'Multiple Choice'),
        (1, 'True or False'),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    method = models.IntegerField(choices=METHOD_CHOICES, default=0, verbose_name="Type of Question")
    title = models.CharField(max_length=140, verbose_name="Title")
    difficulty = models.IntegerField(choices=SCALE_CHOICES, default=0, verbose_name="Level of Difficulty")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    is_active = models.BooleanField(default=False, verbose_name="Active Status")

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=140, verbose_name="Answer Text")
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer_text






