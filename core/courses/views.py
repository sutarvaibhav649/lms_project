from django.shortcuts import render, HttpResponse

# Create your views here.
def course_list(request):
    return render (request,'course_list.html')

def lesson_list(request):
    return render(request,'lesson_details.html')