import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.0)
height = st.number_input("Enter your height (m):", min_value=0.0)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"Category: {category}")
    else:
        st.write("Please enter valid weight and height.")

