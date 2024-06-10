from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll','field_of_study', 'result']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'roll': 'Roll',
            'field_of_study': 'Field of Study',
            'result': 'CGPA',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'result': forms.NumberInput(attrs={'class': 'form-control'}),
        }