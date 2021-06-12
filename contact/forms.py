from django import forms
from contact.models import Contact
from captcha.fields import CaptchaField

class ContactModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message'}),
        }
