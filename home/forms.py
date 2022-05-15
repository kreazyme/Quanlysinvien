from dataclasses import field
from pyexpat import model
from django.forms import ModelForm, forms
from .models import Student
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [ 
            'code',
            'name',
            'address',
            'age',
            'email',
        ]