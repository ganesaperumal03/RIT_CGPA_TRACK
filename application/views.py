from django.shortcuts import render, redirect, get_object_or_404
from application.form import basic_course_details_form,course_grade_form,cgpa_track_form
from application.models import course_details,course_grade,cgpa_track
from datetime import datetime
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.conf import settings
import pandas as pd
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.shortcuts import render, get_object_or_404, HttpResponse

def index(request):
    return render(request, "index.html")

def course_index(request):

    if request.method == 'POST':
        batch = request.POST.get('batch')
        semester = request.POST.get('semester')
        Department = request.POST.get('Department')
        course_count = request.POST.get('course_count')
        print(semester,batch)
        print('yes')
        course_dict={"batch":batch,"semester":semester,"Department":Department,"course_count":course_count}

        request.session['course_data'] =course_dict
        return redirect('insert_course_details')
    print('NO')

    return render(request, "staff/index.html")

def insert_course_details(request):
    course_data=request.session.get('course_data', {})
    batch = course_data['batch']
    semester =course_data['semester']
    Department = course_data['Department']
    course_count =int(course_data['course_count'])
    course_code_values = []
    course_grade_data_check= course_grade.objects.filter( Reg_no=Reg_no, batch=batch, semester=semester, department=Department)

    if request.method == 'POST':
        form = basic_course_details_form(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.batch = batch 
            user.semester = semester
            user.Department = Department
            user.course_count = course_count

            user.save()
            return redirect('course_index')

        else:
            return render(request, "staff/error.html", {'form': form})
    return render(request, "staff/course_details.html", {"total": range(course_count)})


def student_index(request):

    if request.method == 'POST':
        batch = request.POST.get('batch')
        semester = request.POST.get('semester')
        Department = request.POST.get('Department')
        Reg_no = request.POST.get('Reg_no')
        student_name = request.POST.get('student_name')

        print(semester,batch)
        print('yes')
        course_dict={"batch":batch,"semester":semester,"Department":Department,'student_name':student_name,"Reg_no":Reg_no}

        request.session['grade_data'] =course_dict
        return redirect('add_course_grade')
    print('NO')

    return render(request, "student/index.html")


def add_course_grade(request):
    grade_data=request.session.get('grade_data', {})
    batch = grade_data['batch']
    semester =grade_data['semester']
    Department = grade_data['Department']
    student_name = grade_data['student_name']
    Reg_no = grade_data['Reg_no']
    print(Reg_no)

    course_grade_data_check = course_details.objects.filter(  batch=batch,semester=semester,Department=Department)
    
    if not course_grade_data_check:
        return HttpResponse("Not updating course code and course credits ", status=400)

    course_grade_data = get_object_or_404(course_details, batch=batch,semester=semester,Department=Department)

    
    course_grade_data_check= course_grade.objects.filter( Reg_no=Reg_no, batch=batch, semester=semester, department=Department)
    print(course_grade_data_check)
    
    if course_grade_data_check:
        course_grade_data_value = get_object_or_404(course_grade, Reg_no=Reg_no, semester=semester,batch=batch, department=Department)
    

    course_count_data=int(course_grade_data.course_count)
    course_code_values = []

    for i in range(1, course_count_data + 1):
        course_code_attr = f'coursecode{i}'
        course_grade_attr = f'coursegrade{i}'
        print(course_grade_attr)

        course_code_attr = getattr(course_grade_data, course_code_attr, None)
        if course_grade_data_check:
            course_grade_attr = getattr(course_grade_data_value, course_grade_attr, None)
            print(course_grade_attr)
        else:
            course_grade_attr=None
            
        if course_code_attr and course_grade_attr is not None:
            course_code_values.append({"code":course_code_attr,'grade':course_grade_attr})
        if course_grade_attr is None:
            course_code_values.append({"code":course_code_attr})


    print(course_code_values)

    if request.method == 'POST':
        form = course_grade_form(request.POST)
        course_cgpa_data_check = course_grade.objects.filter( Reg_no=Reg_no, batch=batch, student_name=student_name, semester=semester,department=Department)
        if form.is_valid():
            if not course_cgpa_data_check.exists():
                new_grade = form.save(commit=False)
                new_grade.coursegrade1 = form.cleaned_data['coursegrade1']
                new_grade.coursegrade2 = form.cleaned_data['coursegrade2']
                new_grade.coursegrade3 = form.cleaned_data['coursegrade3']
                new_grade.coursegrade4 = form.cleaned_data['coursegrade4']
                new_grade.coursegrade5 = form.cleaned_data['coursegrade5']
                new_grade.coursegrade6 = form.cleaned_data['coursegrade6']
                new_grade.coursegrade7 = form.cleaned_data['coursegrade7']
                new_grade.coursegrade8 = form.cleaned_data['coursegrade8']
                new_grade.coursegrade9 = form.cleaned_data['coursegrade9']
                new_grade.coursegrade10 = form.cleaned_data['coursegrade10']
                new_grade.coursegrade11 = form.cleaned_data['coursegrade11']
                new_grade.coursegrade12 = form.cleaned_data['coursegrade12']
                new_grade.batch = batch
                new_grade.semester = semester
                new_grade.department = Department
                new_grade.student_name = student_name
                new_grade.Reg_no = Reg_no
                new_grade.course_count = course_count_data
                new_grade.save()
                
            else:
                grade_update = get_object_or_404(course_grade, Reg_no=Reg_no, semester=semester,batch=batch, student_name=student_name, department=Department)

                grade_update.course_count = course_count_data
                grade_update.coursegrade1 = form.cleaned_data['coursegrade1']
                grade_update.coursegrade2 = form.cleaned_data['coursegrade2']
                grade_update.coursegrade3 = form.cleaned_data['coursegrade3']
                grade_update.coursegrade4 = form.cleaned_data['coursegrade4']
                grade_update.coursegrade5 = form.cleaned_data['coursegrade5']
                grade_update.coursegrade6 = form.cleaned_data['coursegrade6']
                grade_update.coursegrade7 = form.cleaned_data['coursegrade7']
                grade_update.coursegrade8 = form.cleaned_data['coursegrade8']
                grade_update.coursegrade9 = form.cleaned_data['coursegrade9']
                grade_update.coursegrade10 = form.cleaned_data['coursegrade10']
                grade_update.coursegrade11 = form.cleaned_data['coursegrade11']
                grade_update.coursegrade12 = form.cleaned_data['coursegrade12']
                grade_update.save()
                # Grade dictionary
            grade_dict = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "UL": 0}
            
            # Initialize variables for credits and grade values
            total_credits = 0
            credits_values = []
            grade_values = []

            # Get course credits data
            course_credits_data = get_object_or_404(course_details, semester=semester,batch=batch, Department=Department)

            course_count_data = int(course_credits_data.course_count)
            for i in range(1, course_count_data + 1):
                coursecredits_attr = f'coursecredits{i}'
                course_credit_value = getattr(course_credits_data, coursecredits_attr, None)
                if course_credit_value is not None:
                    course_credit_value = int(course_credit_value)
                    credits_values.append(course_credit_value)
                    total_credits += course_credit_value

            # Get course grade data
            course_cgpa_data = get_object_or_404(course_grade, Reg_no=Reg_no, batch=batch, student_name=student_name, semester=semester,department=Department)
            print(course_cgpa_data)
            for i in range(1, course_count_data + 1):
                course_grade_attr = f'coursegrade{i}'
                course_grade_value = getattr(course_cgpa_data, course_grade_attr, None)
                print(course_grade_value)
                if course_grade_value is not None:
                    grade_point = grade_dict[course_grade_value]
                    print("grade_point",grade_point)
                    if grade_point is not None:
                        grade_values.append(grade_point)
                        print(f"Total Credits: {total_credits}",grade_values)

            print(f"Total Credits: {total_credits}",grade_values)

            # Calculate GPA
            if total_credits == 0 or not grade_values:
                return HttpResponse("Error in calculating GPA: No valid course data.", status=400)
            print('credits_values',credits_values)
            print('grade_values',grade_values)

            weighted_sum = sum(credits_values[i] * grade_values[i] for i in range(len(credits_values)))
            gpa = weighted_sum / total_credits
            gpa = round(gpa, 3)

            print(f"Total Credits: {total_credits}")
            print(f"GPA: {gpa}")
            form = cgpa_track_form(request.POST)
            cgpa_value_check = cgpa_track.objects.filter( Reg_no=Reg_no, batch=batch, student_name=student_name, department=Department)
            if cgpa_value_check:
                print(f"Total Credits: {total_credits}")
                print(f"GPA: {gpa}")
                print("--------------------------------------")
                cgpa_value = get_object_or_404(cgpa_track, Reg_no=Reg_no, batch=batch, student_name=student_name, department=Department)
                sem1 = float(cgpa_value.semester1) if cgpa_value.semester1 is not None else None
                sem2 = float(cgpa_value.semester2) if cgpa_value.semester2 is not None else None
                sem3 = float(cgpa_value.semester3) if cgpa_value.semester3 is not None else None
                sem4 = float(cgpa_value.semester4) if cgpa_value.semester4 is not None else None
                sem5 = float(cgpa_value.semester5) if cgpa_value.semester5 is not None else None
                sem6 = float(cgpa_value.semester6) if cgpa_value.semester6 is not None else None
                sem7 = float(cgpa_value.semester7) if cgpa_value.semester7 is not None else None
                sem8 = float(cgpa_value.semester8) if cgpa_value.semester8 is not None else None
                

                if semester=='1st_semester':
                    cgpa_value.semester1 = gpa
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8


                elif semester=='2nd_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = gpa
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8
                elif semester=='3rd_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = gpa
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8
                elif semester=='4th_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = gpa
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8
                elif semester=='5th_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = gpa
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8
                elif semester=='6th_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = gpa
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = sem8
                elif semester=='7th_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = gpa
                    cgpa_value.semester8 = sem8
                elif semester=='8th_semester':
                    cgpa_value.semester1 = sem1
                    cgpa_value.semester2 = sem2
                    cgpa_value.semester3 = sem3
                    cgpa_value.semester4 = sem4
                    cgpa_value.semester5 = sem5
                    cgpa_value.semester6 = sem6
                    cgpa_value.semester7 = sem7
                    cgpa_value.semester8 = gpa
                sem1 = float(cgpa_value.semester1) if cgpa_value.semester1 is not None else None
                sem2 = float(cgpa_value.semester2) if cgpa_value.semester2 is not None else None
                sem3 = float(cgpa_value.semester3) if cgpa_value.semester3 is not None else None
                sem4 = float(cgpa_value.semester4) if cgpa_value.semester4 is not None else None
                sem5 = float(cgpa_value.semester5) if cgpa_value.semester5 is not None else None
                sem6 = float(cgpa_value.semester6) if cgpa_value.semester6 is not None else None
                sem7 = float(cgpa_value.semester7) if cgpa_value.semester7 is not None else None
                sem8 = float(cgpa_value.semester8) if cgpa_value.semester8 is not None else None
                if sem8 is not None:
                    cgpa=(sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8
                elif sem7 is not None:
                    cgpa=(sem1+sem2+sem3+sem4+sem5+sem6+sem7)/7
                elif sem6 is not None:
                    cgpa=(sem1+sem2+sem3+sem4+sem5+sem6)/6
                elif sem5 is not None:
                    cgpa=(sem1+sem2+sem3+sem4+sem5)/5
                elif sem4 is not None:
                    cgpa=(sem1+sem2+sem3+sem4)/4
                elif sem3 is not None:
                    cgpa=(sem1+sem2+sem3)/3
                elif sem2 is not None:
                    cgpa=(sem1+sem2)/2
                elif sem1 is not None:
                    cgpa=sem1
                print('update',cgpa)

                cgpa_value.batch = batch 
                cgpa_value.department = Department
                cgpa_value.student_name = student_name
                cgpa_value.Reg_no = Reg_no
                cgpa_value.cgpa = cgpa
                cgpa_value.save()
                return redirect('student_index')
            else:
                cgpa=gpa
                if form.is_valid():
                    user = form.save(commit=False)
                    user.batch = batch 
                    user.department = Department
                    user.student_name = student_name
                    user.Reg_no = Reg_no
                    user.cgpa = cgpa

                    if semester=='1st_semester':
                        user.semester1 = gpa
                    elif semester=='2st_semester':
                        user.semester2 = gpa
                    elif semester=='3rd_semester':
                        user.semester3 = gpa
                    elif semester=='4th_semester':
                        user.semester4 = gpa
                    elif semester=='5th_semester':
                        user.semester5 = gpa
                    elif semester=='6th_semester':
                        user.semester6 = gpa
                    elif semester=='7th_semester':
                        user.semester7 = gpa
                    elif semester=='8th_semester':
                        user.semester8 = gpa
                    user.save()

                else:
                    return render(request, "staff/error.html", {'form': form})
                return redirect('student_index')

        else:
            return render(request, "staff/error.html", {'form': form})
    return render(request, "student/add_course_grade.html", {"total": range(course_count_data),"course_grade_data":course_grade_data,"course_code_values":course_code_values})




def hod_index(request):

    if request.method == 'POST':
        batch = request.POST.get('batch')
        Department = request.POST.get('Department')
        course_dict={"batch":batch,"Department":Department}

        request.session['cgpa_track_data'] =course_dict
        return redirect('cgpa_view')

    return render(request, "Hod/index.html")

def cgpa_view(request):
    cgpa_track_data=request.session.get('cgpa_track_data', {})
    batch = cgpa_track_data['batch']
    Department = cgpa_track_data['Department']
    cgpa_track_data = cgpa_track.objects.filter( batch=batch,department=Department)

    return render(request, "Hod/cgpa_track.html",{"cgpa_track_data":cgpa_track_data})

