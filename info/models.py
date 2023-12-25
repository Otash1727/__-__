from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist 


class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.FloatField()
    duration=models.CharField(max_length=255)
    logo_url=models.URLField(max_length=255,null=True,blank=True)
    create_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    



class Users(models.Model):
    tg_id=models.IntegerField()
    user_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=13)
    active_courses=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    extra_role=models.CharField(max_length=50,null=True,blank=True)
    payments=models.CharField(max_length=255,null=True,blank=True)
    invite_people=models.IntegerField(null=True,blank=True)
    cashback=models.FloatField(null=True,blank=True)
    debt=models.FloatField(null=True,blank=True)
    create_at=models.DateTimeField(default=timezone.now)
    users=models.ForeignKey(to=Courses,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.user_name
    
class Groups(models.Model):
    title=models.CharField(max_length=50)
    student_qty=models.IntegerField()
    teacher_name=models.CharField(max_length=100)
    create_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Group={self.title}\nTeacher={self.teacher_name}"
    

  

    
