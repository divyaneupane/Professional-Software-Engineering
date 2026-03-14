from django.shortcuts import render
from .forms import BMIForm

def calculate_bmi(request):
    result = None
    category = None
    form = BMIForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Get height in cm from form and convert to meters
        height_cm = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        height_m = height_cm / 100  # Convert height from cm to meters
        
        # Calculate BMI
        bmi = round(weight / (height_m ** 2), 2)

        # Categorize the BMI value
        if bmi < 20:
            category = "Underweight"
        elif 20 <= bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"

        result = bmi  # Store the BMI value

    return render(request, 'bmi_app/bmi_form.html', {
        'form': form,
        'result': result,
        'category': category
    })