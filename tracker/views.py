import os

from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import User, Assignment, Student
from .forms import StudentSignUpForm, TeacherSignUpForm, StudentInterestsForm, AssignmentForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request, HttpResponseRedirect, Http404
from django.utils import timezone



def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('tracker:assignmentlist')
        else:
            #return redirect('tracker:tasklist')
            return redirect('tracker:grade')
    return render(request, 'tracker/home.html')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'tracker/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tracker:assignmentlist')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'tracker/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return redirect('tracker:tasklist')


class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = 'tracker/interests_form.html'
    success_url = reverse_lazy('tracker:tasklist')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = ('title', 'grade', 'filename','duedate',)
    template_name = 'tracker/assigment_add_form.html'

    def form_valid(self, form):
        assignment = form.save(commit=False)
        assignment.owner = self.request.user
        assignment.save()
        #request.session['title'] = assignment
        messages.success(self.request, 'The assignment was created with success!.')
        #return redirect('tracker:assignmentlist')
        return redirect('tracker:upload' ,pk=assignment.pk)

def assignmentlist(request):
    assignments = list(Assignment.objects.filter(owner=request.user))
    context = {'assignments':assignments}
    return render(request,'tracker/assignment_list.html',context)

def grade(request):
    #return  HttpResponse("here")
    return render(request,'tracker/grade.html')

def tasklist(request):
    if request.method == 'POST':
        grade = request.POST['grade']
        assignments = list(Assignment.objects.filter(grade=grade))
        submission_date  = timezone.now()
        context = {'assignments':assignments,'submission_date':submission_date}
        return render(request,'tracker/task_list.html',context)
    else:
        #return  HttpResponse("else")
        return render(request,'tracker/grade.html')

def upload(request,pk):
    if request.method == 'POST':
        print(request.method)
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        Assignment.objects.filter(pk=pk).update(filename=uploaded_file.name)
        return redirect('tracker:assignmentlist')
    else:
        print(request.method)
    return render(request,'tracker/upload.html')


def solutionupload(request,pk):
    if request.method == 'POST':
        print(request.method)
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        return redirect('tracker:tasklist')
    else:
        print(request.method)
    return render(request,'tracker/solutionupload.html')

