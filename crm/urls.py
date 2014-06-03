from django.conf.urls import patterns, url
from crm import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^teacher/(?P<teacher_id>\d+)/$',views.teacher_info,name='teacher_info'),
	url(r'^teacher/add/$',views.add_teacher,name='add_teacher'),
	url(r'^teacher/create/$',views.create_teacher,name='create_teacher'),
	url(r'^teacher/edit/(?P<teacher_id>\d+)/$',views.edit_teacher, name= 'edit_teacher'),
	url(r'^teacher/modify/(?P<teacher_id>\d+)/$',views.modify_teacher, name='modify_teacher'),
	url(r'^teacher/delete/(?P<teacher_id>\d+)/$',views.delete_teacher,name='delete_teacher'),

	#student
	url(r'^student/(?P<student_id>\d+)/$',views.student_info,name='student_info'),
	url(r'^student/add/$',views.add_student,name='add_student'),
	url(r'^student/create/$',views.create_student,name='create_student'),
	url(r'^student/edit/(?P<student_id>\d+)/$',views.edit_student, name= 'edit_student'),
	url(r'^student/modify/(?P<student_id>\d+)/$',views.modify_student, name='modify_student'),
	url(r'^student/delete/(?P<student_id>\d+)/$',views.delete_student,name='delete_student'),

	#performance
	url(r'^performance/(?P<student_id>\d+)/(?P<p_id>\d+)/$',views.performance,name='performance'),
	url(r'^performance/(?P<student_id>\d+)/add/$',views.add_performance,name='add_performance'),
	url(r'^performance/create/$',views.create_performance,name='create_performance'),
	url(r'^performance/delete/(?P<performance_id>\d+)/$',views.delete_performance,name='delete_performance'),
	
	#search
	url(r'^search/(?P<keyword>.+)/$',views.search_info,name='search'),
    url(r'^ajax_search/(?P<keyword>.+)/$',views.ajax_search,name='ajax_search'), 
)