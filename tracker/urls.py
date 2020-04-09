from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('assignmentlist/', views.assignmentlist, name = 'assignmentlist'),
    path('tasklist/', views.tasklist, name='tasklist'),
    #path('tasklist/', views.TaskListView.as_view(), name='tasklist'),
    path('interests/', views.StudentInterestsView.as_view(), name='student_interests'),
    path('assignment/add/', views.AssignmentCreateView.as_view(), name='assignment_add'),
    path('upload/<int:pk>',views.upload,name='upload'),
    path('solutionupload/<int:pk>',views.solutionupload,name='solutionupload'),
    path('grade/', views.grade, name='grade'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
