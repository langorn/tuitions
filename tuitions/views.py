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

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                print 'useris active'
                login(request, user)
                return HttpResponseRedirect('/crm')
            else:
                return HttpResponse("Error")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('crm/login.html', {}, context)