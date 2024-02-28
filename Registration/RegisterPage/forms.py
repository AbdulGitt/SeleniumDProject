from django import forms

from .models import MyEmployeeData


# Create your models here.
class MyEmployeeForm(forms.ModelForm):
   class Meta:
       model=MyEmployeeData
       fields="__all__"
