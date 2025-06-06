from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.lesson)
admin.site.register(models.LessonProgress)
admin.site.register(models.Track)
admin.site.register(models.TrackCourse)
admin.site.register(models.Leaderboard)
admin.site.register(models.ProgressReport)