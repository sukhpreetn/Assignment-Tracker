from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    #path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),

]