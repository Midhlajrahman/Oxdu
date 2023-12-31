# web/forms.py
from django import forms
from django.forms import widgets
from .models import Contact, CourseRegistration, Register


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Phone"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your subject"}
            ),
            "email": widgets.EmailInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Email Address",
                }
            ),
            "message": widgets.Textarea(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Type Your Message",
                }
            ),
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ("timestamp", "event_title")  # Make sure event_title is excluded

        widgets = {
            "full_name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required form-control", "placeholder": "Your Email"}
            ),
            "location": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Location"}
            ),
            "contact_number": widgets.TextInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Contact Number",
                }
            ),
            "event": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "event"}
            ),
        }

        labels = {
            "full_name": "Full Name",
            "email": "Email",
            "location": "Location",
            "contact_number": "Contact Number",
            "event": "event",
        }


class RegisterationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        exclude = ("timestamp",)

        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required form-control", "placeholder": "Your Email"}
            ),
            "phone": widgets.NumberInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Contact Number",
                }
            ),
            "course": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "course"}
            ),
        }

        labels = {
            "name": "name",
            "email": "email",
            "phone": "phone",
        }
