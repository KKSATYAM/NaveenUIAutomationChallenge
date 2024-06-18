from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    dob=forms.DateField()

