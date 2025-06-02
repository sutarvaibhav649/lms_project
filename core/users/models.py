from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
##================= User Model starts ========================
USER_ROLE_CHOICE = (
    ("student","Student"),
    ("faculty","Faculty"),
    ("admin","Admin"),
)
class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=USER_ROLE_CHOICE)
    phone_no = models.CharField(max_length=10,unique=True,null=False,blank=False)
    profile_image = models.ImageField(upload_to="profile/",blank=True,null=True)
    
    def __str__(self):
        return f"{self.username}-{self.role}"
##================= User Model ends ========================

##================= Student Model Starts =======================
class Student(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prn = models.CharField(max_length=10,unique=True,null=False,blank=False)
    department = models.CharField(max_length=50,blank=False,null=False)
    student_class = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.user.username

##================= Student Model Ends =======================

##================= Faculty Model Starts =======================
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.user.username
##================= Faculty Model Ends =======================

    