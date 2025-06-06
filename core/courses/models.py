from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
##======================= Course Model Starts ========================
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    course_duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
##======================= Course Model Ends ==========================

##======================= Lesson Model Starts ========================

class lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lesson')
    lesson_name = models.CharField(max_length=50)
    content = models.TextField()
    video_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.lesson_name} - {self.course.course_name}"
##======================= Lesson Model Ends ==========================

##======================= Track Model Starts =========================

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

##======================= Track Model Ends ===========================

##======================= Track Course Model Starts ===========================
class TrackCourse(models.Model):
    track = models.ForeignKey(Track,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.track.name}-{self.course.course_name}"

##======================= Track Course Model Ends =============================

##======================= Lesson Progrss model Starts =========================

class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ('user','lesson')
    
    def __str__(self):
        return f"{self.user.username} - {self.lesson.lesson_name} - {'Done' if self.is_completed else 'Pending'}"
##======================= Lesson Progrss model Ends ===========================

##======================= Leaderboard Model Starts ============================
class Leaderboard(models.Model):
    leader_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    updated_at = models.DateField(auto_now=False)
    
    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"

##======================= Leaderboard Model Starts ============================

##======================= Progress Report Model Starts ========================

class ProgressReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now_add=True)
    completed_lessons = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.report_date}"

##======================= Progress Report Model Ends ==========================