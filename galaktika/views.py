from django.shortcuts import render, redirect, get_object_or_404
from . import models
# Create your views here.

from . import forms


def index(request, pk=None):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            # Handle courses and filliallar separately
            return redirect("galaktika:index")
    else:
        form = forms.ContactForm()
        
        
    advantages = models.Advantages.objects.all()
    categories = models.CategoryContent.objects.all()
    if pk:
        qiziqarli = models.Content.objects.filter(category__pk=pk)
    else:
        qiziqarli = models.Content.objects.all()
    facts = models.About.objects.all()
    courses = models.Course.objects.all()
    counts = models.Learners_count.objects.all()
    
    
    context = {
        "advantages":advantages,
        "categories":categories,
        "qiziqarli":qiziqarli,
        "facts":facts,
        "courses":courses,
        "counts":counts,
        "active":"index",
        "form":form
    }
    return render(request, "galaktika/index.html", context=context)




def about(request):
    
    
    facts = models.About.objects.all()
    
    
    context = {
        "facts":facts,
        
        "active":"about"
    }
    return render(request, "galaktika/about.html", context=context)


def interesting(request):
    categories = models.CategoryContent.objects.all()
    qiziqarli = models.Content.objects.all()
    
    
    context = {
        "categories":categories,
        "qiziqarli":qiziqarli,
        "active":"interesting"
    }
    return render(request, "galaktika/interesting.html", context=context)


def courses(request):
    courses = models.Course.objects.all()
    categories = models.CategoryCourse.objects.all()
    
    
    context = {
       
        "courses":courses,
        "categories":categories,
        "active":"courses"
        
    }
    
    return render(request, "galaktika/courses.html", context=context)


def teachers(request):
    teachers = models.Teacher.objects.all()
    fillial = models.Fillial.objects.all()
    
    context = {
        "categories":fillial,
        "teachers": teachers,
        "active":"teachers"
    }
    
    return render(request, "galaktika/teachers.html", context=context)


def contact(request):
    
    
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            # Handle courses and filliallar separately
            return redirect("galaktika:index")
    else:
        form = forms.ContactForm()
    
    
    context = {
        "form":form,
    }
    return render(request, "galaktika/contact.html", context=context)




def teacher_detail(request, pk):
    teacher = get_object_or_404(models.Teacher, pk=pk)
    
    context = {
        "teacher":teacher
    }
    return render(request, "galaktika/teacher_detail.html", context=context)




def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    
    context = {
        "course":course
    }
    return render(request, "galaktika/course_detail.html", context=context)



def post_detail(request, pk):
    content = get_object_or_404(models.Content, pk=pk)
    
    context = {
        "content":content
    }
    return render(request, "galaktika/post_detail.html", context=context)



