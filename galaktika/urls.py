from django.urls import path

from . import views

app_name = "galaktika"


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("interesting/", views.interesting, name="interesting"),
    path("courses/", views.courses, name="courses"),
    path("teachers/", views.teachers, name="teachers"),
    path("contact/", views.contact, name="contact"),
    path("teacher_detail/<int:pk>/", views.teacher_detail, name="teacher_detail"),
    path("course_detail/<int:pk>/", views.course_detail, name="course_detail"),
    path("post_detail/<int:pk>/", views.post_detail, name="post_detail")
]