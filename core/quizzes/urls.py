from django.urls import include, path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('',view=views.quiz_page,name='quiz_page')
]