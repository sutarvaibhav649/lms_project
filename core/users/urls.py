from django.urls import path
from . import views

urlpatterns = [
    path('register/', view=views.register_view, name='register'),
    path('login/', view=views.login_view, name='login'),
    path('logout/', view=views.logout_view, name='logout'),
    path('student/dashboard/', view=views.student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', view=views.faculty_dashboard, name='faculty_dashboard'),
    path('admin/dashboard/', view=views.admin_dashboard, name='admin_dashboard'),
]