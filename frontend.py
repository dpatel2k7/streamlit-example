
import streamlit as st

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

            st.session_state.bmi = bmi
            st.session_state.state = State.BMI_RESULT

def display_bmi_result():
    bmi = st.session_state.bmi
    recommendations = get_recommendations(bmi)
    st.write(recommendations)
    

def calculate_bmi(weight_kg, height_meters):
    return weight_kg / (height_meters ** 2)

def get_recommendations(bmi):
    if bmi < 18.5:
        return "You are underweight. Consider consuming more calories and protein-rich foods."
    elif 18.5 <= bmi < 25:
        return "You have a normal weight. Keep maintaining a balanced diet and regular exercise routine."
    elif 25 <= bmi < 30:
        return "You are overweight. Focus on portion control, increase physical activity, and consume more whole foods."
    else:
        return "You are obese. Consult a healthcare professional for personalized advice and focus on gradual weight loss through diet and exercise."

def main():
    if "state" not in st.session_state:
        st.session_state.state = State.INPUT_FORM

    bmi_calculator()

if __name__ == "__main__":
    main()