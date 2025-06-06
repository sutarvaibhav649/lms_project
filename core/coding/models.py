from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
##======================= Codding Challenge Model Starts =========================

class CodingChallenge(models.Model):
    challenge_id = models.AutoField(primary_key=True)
    challenge_name = models.CharField(max_length=150)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.challenge_name} ({self.difficulty})"

##======================= Codding Challenge Model Ends ===========================

##======================= Badges Model Starts ===========================

class Badge(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    criteria = models.TextField()
    icon = models.ImageField(upload_to='badges/', blank=True, null=True)

    def __str__(self):
        return self.name

##======================= Badges Model Ends =============================

##======================= User Badges Model Starts ======================

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'badge')

    def __str__(self):
        return f"{self.user.username} earned {self.badge.name}"

##======================= User Badges Model Ends ========================