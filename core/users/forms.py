from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Faculty,User

##================== Custome user Form starts ===========================
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','role','phone_no','profile_image']
##================== Custome user Form ends =============================

##================== Studemt form starts ====================
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['prn','department','student_class']
##================== Studemt form ends ======================
##================== Faculty form starts ====================
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['department']
##================== Faculty form ends ======================