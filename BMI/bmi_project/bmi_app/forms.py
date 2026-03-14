from django import forms

class BMIForm(forms.Form):
    height = forms.FloatField(label='Height (cm)', min_value=0.5, max_value=300)
    weight = forms.FloatField(label='Weight (kg)', min_value=10, max_value=300)