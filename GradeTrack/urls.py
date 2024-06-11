"""
URL configuration for GradeTrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course_index', views.course_index, name="course_index"),
    path('insert_course_details', views.insert_course_details, name="insert_course_details"),
    path('student_index', views.student_index, name="student_index"),
    path('add_course_grade', views.add_course_grade, name="add_course_grade"),
    path('hod_index', views.hod_index, name="hod_index"),
    path('cgpa_view', views.cgpa_view, name="cgpa_view"),
    path('', views.index, name="index"),

]
