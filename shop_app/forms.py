from django import forms
from django.forms import ModelForm
from .models import Info
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Info
        exclude = ['user']
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'DOB':forms.DateInput(attrs={'class':'form-control'}),
        }