from django.db import models
from courses import models as cmd
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
##===================== Assignments Model Starts =======================

class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(cmd.Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course.course_name}"

##===================== Assignments Model Ends =========================

##===================== Submission Model Starts ========================class Submission(models.Model):
class Submission(models.Model):
    sub_id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_file = models.FileField(upload_to='submissions/')
    sub_date = models.DateTimeField(auto_now_add=True)
    sub_marks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.assignment.title}"

##===================== Submission Model Ends ==========================