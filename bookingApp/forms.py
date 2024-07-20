from django import forms
from .models import Appartment

class AvailabilityForm(forms.Form):

    # appart_list =forms.ModelChoiceField(queryset=Appartment.objects.all(),empty_label="select_appartement")
    check_in = forms.DateTimeField(required=True,input_formats=['%Y-%m-%d %H:%M'],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out = forms.DateTimeField(required=True,input_formats=["%Y-%m-%d %H:%M"],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


class ContactForm(forms.Form):
    first_name= forms.CharField(max_length=255)
    last_name= forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)