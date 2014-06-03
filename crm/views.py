from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from crm.forms import UserForm, UserProfileForm
from django.db.models import Q
from django.core import serializers
import json

from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder

from crm.models import Student, Teacher,Performance
from crm.models import StudentForm , TeacherForm, PerformanceForm
# Create your views here.

def index(request):
	return render(request, 'crm/index.html')

@login_required
def search_info(request, keyword):
	if keyword == 'teacher':
		result_list = Teacher.objects.all()
	elif keyword == 'student':
		result_list = Student.objects.all()
	else:
		result_list = []
	context = {'result_list':result_list, 'keyword':keyword}
	return render(request, 'crm/index.html',context)

@login_required
def ajax_search(request,keyword):
	result_list = Student.objects.filter(Q(name__contains=keyword)|Q(phone__contains=keyword))
	context = {'result_list':result_list}
	data = serializers.serialize('json', result_list, fields=('name','size'))
	return HttpResponse(data, mimetype="application/json") 

# teacher
@login_required
def teacher_info(request,teacher_id):
	teachers_list = Teacher.objects.get(pk=teacher_id)
	try:
		students_list = Student.objects.filter(teacher = teachers_list)
	except:
		students_list = []
	context = {'teachers_list':teachers_list,'students_list':students_list}
	return render(request, 'crm/teacher_list.html',context)

@login_required
def add_teacher(request):
	form = TeacherForm()
	context = {'form':form}
	return render(request, 'crm/add_teacher.html',context)

@login_required
def create_teacher(request):
	f = TeacherForm(request.POST)
	if f.is_valid():
		new_teacher = f.save(commit=False)
		new_teacher.save()
	return HttpResponseRedirect('/crm/search/teacher/')

@login_required
def edit_teacher(request, teacher_id):
	teacher = Teacher.objects.get(pk = teacher_id)
	form = TeacherForm(instance=teacher)
	context = {'form':form, 'teacher_id':teacher_id}
	return render(request, 'crm/edit_teacher.html', context)

@login_required
def modify_teacher(request,teacher_id):
	teacher = Teacher.objects.get(pk = teacher_id)
	f = TeacherForm(request.POST,instance = teacher)
	if f.is_valid():
		f.save()
	return HttpResponseRedirect('/crm/search/teacher/')

@login_required
def delete_teacher(request, teacher_id):
	teacher = Teacher.objects.get(pk = teacher_id)
	teacher.active = False
	teacher.save()
	return HttpResponseRedirect('/crm')

# student
@login_required
def student_info(request,student_id):
	student_list = Student.objects.get(pk=student_id)
	performance_list = Performance.objects.filter(student=student_list)
	context = {'student_list':student_list ,'performance_list':performance_list}
	return render(request, 'crm/student_list.html',context)

@login_required
def add_student(request):
	form = StudentForm()
	context = {'form':form}
	return render(request, 'crm/add_student.html',context)

@login_required
def create_student(request):
	f = StudentForm(request.POST)
	if f.is_valid():
		new_student = f.save(commit=False)
		new_student.save()
	return HttpResponseRedirect('/crm/search/student/')

@login_required
def edit_student(request, student_id):
	student = Student.objects.get(pk = student_id)
	form = StudentForm(instance=student)
	context = {'form':form, 'student_id':student_id}
	return render(request, 'crm/edit_student.html', context)

@login_required
def modify_student(request,student_id):
	student = Student.objects.get(pk = student_id)
	f = StudentForm(request.POST,instance = student)
	if f.is_valid():
		f.save()
	return HttpResponseRedirect('/crm/search/student/')

@login_required
def delete_student(request, student_id):
	student = Student.objects.get(pk = student_id)
	student.active = False
	student.save()
	return HttpResponseRedirect('/crm')

# performance
@login_required
def performance(request, student_id , p_id):
	return HttpResponse("Performance_id/"+p_id)

@login_required
def add_performance(request, student_id):
	student = Student.objects.get(pk=student_id)
	form = PerformanceForm(instance=student)
	context = {'form':form, 'student':student}
	return render(request, 'crm/add_performance.html',context)

@login_required
def create_performance(request):
	f = PerformanceForm(request.POST)
	if f.is_valid():
		new_performance = f.save(commit=False)
		new_performance.save()
	return HttpResponseRedirect('/crm/search/student/')

@login_required
def delete_performance(request,performance_id):
	performance = Performance.objects.get(pk = performance_id)
	performance.active = False
	performance.save()
	return HttpResponseRedirect('/crm')

#user login
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)




