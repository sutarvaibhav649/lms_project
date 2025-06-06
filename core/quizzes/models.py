from django.db import models
from courses import models as cmd
# Create your models here.
##========================== Quize Model Starts ===========================

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(cmd.Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.course_name})"

##========================== Quize Model Ends =============================

##========================== Quiz Question Model Starts ===================

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return f"Q: {self.question_text[:50]}"

##========================== Quiz Question Model Ends =====================
