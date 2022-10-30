from django import forms
from .models import Apply , job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ["name","email","website","upload_cv","cover_letter"]
        
        
class AddNewJob(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner','slug')