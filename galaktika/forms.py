from django import forms
from . import models
import re

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={"required": 'Ismingizni kiriting'},
        label="Ism",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'})
    )
    
    surname = forms.CharField(
        error_messages={"required": 'Familiyangizni kiriting'},
        label="Familiya",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'})
    )
    
    phone = forms.CharField(
        error_messages={"required": 'Telefon raqam kiriting', "invalid": "To'g'ri raqam kiriting"},
        label="Telefon raqam",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
        validators=[lambda value: re.match(r'^\+998[0-9]{2}[0-9]{7}$', value)]
    )
    
    courses = forms.ModelChoiceField(
        queryset=models.Course.objects.all(),
        required=False,
        label="Kurslar",
        error_messages={'required': 'Qaysi kursga yozilmoqchisiz', 'invalid_choice': "Tog'ri kiriting"},
        widget=forms.Select(attrs={'class': 'form-control', 'value':'Tanlang', 'style':"margin:10px"}),
        empty_label="Kurs"
    )
    
    filliallar = forms.ModelChoiceField(
        queryset=models.Fillial.objects.all(),
        required=False,
        label="Filliallar",
        error_messages={
            'required': 'Fillialni tanlang',
            'invalid_choice': "Tog'ri fillialni tanlang",
        },
        widget=forms.Select(attrs={'class': 'form-control', 'style':"margin:10px"}),
        empty_label="FIllial"
    )

    class Meta:
        model = models.Students
        fields = ['name', 'surname', 'phone', 'courses', 'filliallar']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+998\d{2}\d{3}\d{2}\d{2}$', phone):
            raise forms.ValidationError("Telefon raqamini: +998 ko'rinishida yozing va joy Tashlamang")
        return phone
