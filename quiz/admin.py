from django.contrib import admin
from quiz.models import *
# Register your models here.

@admin.register(quiz)
class quizmodel(admin.ModelAdmin):
    list_display = ('id','name','status')


@admin.register(question)
class questionmodel(admin.ModelAdmin):
    list_display = ('id','quiz','question','answer')

    list_filter = ('quiz',)