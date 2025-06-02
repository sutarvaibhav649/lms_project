from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomeUserForm, StudentForm, FacultyForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
##=================== Register view Starts =======================
def register_view(request):
    user_form = CustomeUserForm()
    student_form = StudentForm()
    faculty_form = FacultyForm()

    if request.method == 'POST':
        user_form = CustomeUserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            role = user.role

            if role == 'student':
                student_form = StudentForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            elif role == 'faculty':
                faculty_form = FacultyForm(request.POST)
                if faculty_form.is_valid():
                    faculty = faculty_form.save(commit=False)
                    faculty.user = user
                    faculty.save()

            return redirect('login')

    return render(request, 'register.html', {
        'user_form': user_form,
        'student_form': student_form,
        'faculty_form': faculty_form
    })
##=================== Register view Ends =========================
##=================== Login view starts ==========================
def login_view(request):
    errors = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        if not username:
            errors['username'] = "Username is required."
        if not password1:
            errors['password1'] = "Password is required."

        if not errors:
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)

                # Redirect by role
                if user.role == 'student':
                    return redirect('student_dashboard')  # Define in your urls/views
                elif user.role == 'faculty':
                    return redirect('faculty_dashboard')
                elif user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    errors['general'] = "Unknown user role."
            else:
                errors['general'] = "Invalid username or password."

    return render(request, 'login.html', {'errors': errors})
##=================== Login view ends ============================
##=================== logout view starts ===========================
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
##=================== logout view ends =============================

##=================== student dashboard starts =====================
@login_required
def student_dashboard(request):
    return HttpResponse("<h1>Student Dashboard</h1>")
##=================== student dashboard ends =====================

##=================== faculty dashboard starts =====================
@login_required
def faculty_dashboard(request):
    return HttpResponse("<h1>Faculty Dashboard</h1>")
##=================== faculty dashboard ends =====================
##=================== admin dashboard starts =====================
@login_required
def admin_dashboard(request):
    return HttpResponse("<h1>Admin Dashboard</h1>")
##=================== admin dashboard ends =====================