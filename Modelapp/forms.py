from django import forms
from Modelapp.models import students
class Studentsform(forms.ModelForm):
      class Meta:
            model=students
            fields='__all__'
