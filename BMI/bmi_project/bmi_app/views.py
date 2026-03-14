from django.shortcuts import render
from .forms import BMIForm
import os
from google import genai  # Gemini API client

def calculate_bmi(request):
    result = None
    category = None
    plan = None
    form = BMIForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Get form data
        height_cm = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']

        # BMI calculation
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        # BMI category
        if bmi < 20:
            category = "Underweight"
        elif 20 <= bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"

        result = bmi

        # --- Gemini API call to generate diet & exercise plan ---
        try:
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

            prompt = f"""
            Create a one-month personalized diet and exercise plan for a {age}-year-old {gender} person 
            with BMI {bmi}. Include daily meal suggestions and exercise routines.
            """

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )
            plan = response.text
        except Exception as e:
            plan = f"Could not generate plan: {e}"

    return render(request, 'bmi_app/bmi_form.html', {
        'form': form,
        'result': result,
        'category': category,
        'plan': plan
    })
