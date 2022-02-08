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
    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )

    TYPE = (
        (0, 'Multiple Choice')
    )

    


