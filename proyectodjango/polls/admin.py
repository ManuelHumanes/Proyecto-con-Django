from random import choice, choices
from tkinter.messagebox import QUESTION
from django.contrib import admin
from .models import Question,Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)