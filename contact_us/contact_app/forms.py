# contact_app/forms.py
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name) or not name.isalpha():
            raise ValidationError("Name should only contain alphabets.")
        return name

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise ValidationError("Message should be at least 10 characters long.")
        return message

