from django import forms
from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.ru'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите вашу задачу',
                'rows': 4
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control'
            })
        }