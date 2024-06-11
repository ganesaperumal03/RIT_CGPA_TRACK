from django.db import models

class course_details(models.Model):
    Department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
    course_count=models.CharField(max_length=100)

    coursecode1 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits1=models.CharField(max_length=100,blank=True,null=True)
    coursecode2 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits2=models.CharField(max_length=100,blank=True,null=True)
    coursecode3 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits3=models.CharField(max_length=100,blank=True,null=True)
    coursecode4 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits4=models.CharField(max_length=100,blank=True,null=True)

    coursecode5 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits5=models.CharField(max_length=100,blank=True,null=True)

    coursecode6 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits6=models.CharField(max_length=100,blank=True,null=True)

    coursecode7 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits7=models.CharField(max_length=100,blank=True,null=True)

    coursecode8 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits8=models.CharField(max_length=100,blank=True,null=True)

    coursecode9 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits9=models.CharField(max_length=100,blank=True,null=True)

    coursecode10 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits10=models.CharField(max_length=100,blank=True,null=True)

    coursecode11 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits11=models.CharField(max_length=100,blank=True,null=True)

    coursecode12 = models.CharField(max_length=100,blank=True,null=True)
    coursecredits12=models.CharField(max_length=100,blank=True,null=True)


class course_grade(models.Model):
    Reg_no=models.CharField(max_length=20)
    batch=models.CharField(max_length=100)
    course_count=models.CharField(max_length=100)

    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    coursegrade1 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade2 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade3 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade4 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade5 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade6 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade7 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade8 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade9 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade10 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade11 = models.CharField(max_length=100,blank=True,null=True)
    coursegrade12 = models.CharField(max_length=100,blank=True,null=True)
    
class cgpa_track(models.Model):
    Reg_no=models.CharField(max_length=20, primary_key=True)
    batch=models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)

    semester1 = models.CharField(max_length=100,blank=True,null=True)
    semester2 = models.CharField(max_length=100,blank=True,null=True)
    semester3 = models.CharField(max_length=100,blank=True,null=True)
    semester4 = models.CharField(max_length=100,blank=True,null=True)
    semester5 = models.CharField(max_length=100,blank=True,null=True)
    semester6 = models.CharField(max_length=100,blank=True,null=True)
    semester7 = models.CharField(max_length=100,blank=True,null=True)
    semester8 = models.CharField(max_length=100,blank=True,null=True)
