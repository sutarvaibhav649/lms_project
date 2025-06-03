from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm, StudentForm, FacultyForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

##======================= Home view Starts ======================

def home_view(request):
    return render(request,'home.html')
##======================= Home view Ends ========================


##=================== Register view Starts =======================
def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        student_form = StudentForm(request.POST, prefix='student')
        faculty_form = FacultyForm(request.POST, prefix='faculty')

        if user_form.is_valid():
            user = user_form.save(commit=False)
            role = user_form.cleaned_data.get('role')
            user.save()

            if role == 'student' and student_form.is_valid():
                student = student_form.save(commit=False)
                student.user = user
                student.save()

            elif role == 'faculty' and faculty_form.is_valid():
                faculty = faculty_form.save(commit=False)
                faculty.user = user
                faculty.save()

            return redirect('login')

    else:
        user_form = CustomUserCreationForm()
        student_form = StudentForm(prefix='student')
        faculty_form = FacultyForm(prefix='faculty')

    return render(request, 'register.html', {
        'user_form': user_form,
        'student_form': student_form,
        'faculty_form': faculty_form,
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
                    return redirect('home')  # Define in your urls/views
                elif user.role == 'faculty':
                    return redirect('home')
                elif user.role == 'admin':
                    return redirect('home')
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