from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'father_name', 'mother_name', 'date_of_birth', 'gender', 'name_of_degree', 'admission_session', 'reg_no', 'batch', 'graduating_session', 'cgpa']
        
        
        labels = {
            'father_name': 'Father\'s Name',
            'mother_name': 'Mother\'s Name',
            'reg_no': 'Reg/Id No',
            'cgpa': 'CGPA',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your Name'}),
            'father_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Father\'s Name'}),
            'mother_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Mother\'s Name'}),
            'date_of_birth': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Date of Birth'}),
            'gender': forms.Select(attrs={'class':'form-control', 'placeholder': 'Select Gender'}),
            'name_of_degree': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name of Degree'}),
            'admission_session': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Admission Session'}),
            'reg_no': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ID No'}),
            'batch': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Batch'}),
            'graduating_session': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Graduating Session'}),
            'cgpa': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CGPA'}),
            
        }