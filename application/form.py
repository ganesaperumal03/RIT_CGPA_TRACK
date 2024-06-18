from django import forms
from .models import course_details,course_grade,cgpa_track


class basic_course_details_form(forms.ModelForm):
    class Meta:
        model = course_details
        fields = '__all__'
        exclude = ['Department','batch','semester',"course_count"] 

class course_grade_form(forms.ModelForm):
    class Meta:
        model = course_grade
        fields = '__all__'
        exclude = ['department','batch','semester','Reg_no','student_name','course_count'] 

class cgpa_track_form(forms.ModelForm):
    class Meta:
        model = cgpa_track
        fields = '__all__'
        exclude = ['department','batch','semester1','Reg_no','student_name','semester2','semester3','semester4','semester5','semester6','semester7','semester8','cgpa'] 