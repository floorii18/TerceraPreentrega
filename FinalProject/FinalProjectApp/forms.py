from django import forms

class SkillsForm(forms.Form):
    Description = forms.CharField()
    Level = forms.CharField()