
import streamlit as st

from backend import get_recommendations
from backend import calculate_bmi

class State:
    INPUT_FORM = "input_form"
    BMI_RESULT = "bmi_result"

def bmi_calculator():
    if st.session_state.state == State.INPUT_FORM:
        display_input_form()
    elif st.session_state.state == State.BMI_RESULT:
        display_bmi_result()

def display_input_form():    
    st.title("BMI Calculator")

# Print the obesity plan chart
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)
    days_active = st.number_input("How many days per week do you typically stay active?", min_value=0, max_value=7, step=1)

    weight_lbs = st.number_input("Enter your weight (in lbs):", min_value=0.0, step=0.1)
    height_inches = st.number_input("Enter your height (in inches):", min_value=0.0, step=0.01)

    if st.button("Calculate BMI"):
        if weight_lbs <= 0 or height_inches <= 0:
            st.error("Please enter valid weight and height.")
        else:
            # Convert weight from lbs to kg
            weight_kg = weight_lbs * 0.453592  # 1 lb = 0.453592 kg
            # Convert height from inches to meters
            height_meters = height_inches * 0.0254  # 1 inch = 0.0254 meters

            bmi = calculate_bmi(weight_kg, height_meters)
            st.write(f"Your BMI is: {bmi:.2f}")

            if st.button("Get Recommendations"):
                recommendations = get_recommendations(bmi)
                # st.session_state.recommendations = recommendations
            # Initialize session state attributes
            if "name" not in st.session_state:
                st.session_state.name = ""

            if "age" not in st.session_state:
                st.session_state.age = 0

            st.session_state.bmi = bmi
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.days_active = days_active
            st.session_state.state = State.BMI_RESULT

def display_bmi_result():
    # Retrieve variables from session state
    bmi = st.session_state.bmi
    name = st.session_state.name  
    age = st.session_state.age
    days_active = st.session_state.days_active
    recommendations = get_recommendations(bmi, name, age, days_active)
    st.markdown("<h2 style='font-family: Times New Roman;'>You are underweight BMI. Consider consuming more calories and protein-rich foods.</h2>")
    st.write(recommendations)

    if st.button("Go to Home"):
        st.session_state.state = State.INPUT_FORM
    
def main():
    if "state" not in st.session_state:
        st.session_state.state = State.INPUT_FORM

    bmi_calculator()

if __name__ == "__main__":
    main()