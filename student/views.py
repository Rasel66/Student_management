from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_name = form.cleaned_data['name']
            new_student_email = form.cleaned_data['email']
            new_student_roll = form.cleaned_data['roll']
            new_student_field_of_study = form.cleaned_data['field_of_study']
            new_student_result = form.cleaned_data['result']

            new_student = Student(
                name = new_student_name,
                email = new_student_email,
                roll = new_student_roll,
                field_of_study = new_student_field_of_study,
                result = new_student_result,
            )

            new_student.save()
            return render(request, 'students/add_student.html',{'form': StudentForm(), 'success':True})
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html',{'form': StudentForm()})

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html',{'form': form, 'success':True})
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html',{'form': form})
def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))
# Create your views here.
