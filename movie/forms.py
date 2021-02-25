from django import forms
from .models import EmpData


class EmpForm(forms.Form):
    name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'your name',
                'class': 'form-control'
            }
        )
    )
    salary = forms.IntegerField(
        label="Enter Mobile NUmber :",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }
        )
    )
# class EmpForm1(forms.ModelForm):
#     class Meta:
#         model = EmpData
#         fileds = '__all__'




