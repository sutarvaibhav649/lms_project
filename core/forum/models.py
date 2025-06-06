from django.db import models
from courses import models as cmd
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(cmd.Course, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course.course_name}"
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.thread.title[:30]}"

