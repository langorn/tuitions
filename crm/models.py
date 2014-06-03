from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	#working_from = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Student(models.Model):
	teacher = models.ForeignKey(Teacher)
	name = models.CharField(max_length=200)
	birth = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	gender = models.IntegerField(default=1)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Performance(models.Model):
	student = models.ForeignKey(Student)
	title = models.CharField(max_length=200)
	score = models.IntegerField()
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class TeacherForm(ModelForm):
	class Meta:
		model = Teacher


class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['teacher','name','birth','phone','address']


class PerformanceForm(ModelForm):
	class Meta:
		model = Performance


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=128, null= True,blank=True)
    
    def __unicode__(self):
        return self.user.username		