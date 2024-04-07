
import streamlit as st

# Function to render BMI calculator and recommendations
def bmi_calculator():
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

            recommendations_placeholder = st.empty()  # Placeholder for recommendations

            if st.button("Get Recommendations"):
                recommendations = get_recommendations(bmi)
                recommendations_placeholder.write(recommendations)

            st.write(
                """
                Here's some additional information about BMI and a visual representation of BMI categories:
                """
            )

            bmi_chart = st.image("bmi_chart.jpg", use_column_width=True)  # You can replace "bmi_chart.jpg" with your own image file

            st.write(
                """
                According to the World Health Organization (WHO), the BMI categories are as follows:

                - Underweight: BMI less than 18.5
                - Normal weight: BMI 18.5–24.9
                - Overweight: BMI 25–29.9
                - Obesity: BMI 30 or greater
                """
            )

# Function to calculate BMI based on weight (in kg) and height (in meters)
def calculate_bmi(weight_kg, height_meters):
    bmi = weight_kg / (height_meters ** 2)
    return bmi

# Function to generate recommendations based on BMI
def get_recommendations(bmi):
    recommendations = ""
    if bmi < 18.5:
        recommendations = "You are underweight. Consider consuming more calories and protein-rich foods."
    elif 18.5 <= bmi < 25:
        recommendations = "You have a normal weight. Keep maintaining a balanced diet and regular exercise routine."
    elif 25 <= bmi < 30:
        recommendations = "You are overweight. Focus on portion control, increase physical activity, and consume more whole foods."
    else:
        recommendations = "You are obese. Consult a healthcare professional for personalized advice and focus on gradual weight loss through diet and exercise."

    return recommendations

# Main function to run the Streamlit app
def main():
    bmi_calculator()

if __name__ == "__main__":
    main()



# image read sample
# bmi_chart = plt.imread("bmi_chart.jpg")  # You can replace "bmi_chart.jpg" with your own image file
# st.image(bmi_chart, use_column_width=True)


#Version 1
# import streamlit as st

# from backend import calculate_bmi, get_recommendations

# # Function to render BMI calculator and recommendations
# def bmi_calculator():
#     st.title("BMI Calculator")

#     weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
#     height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01)

#     if st.button("Calculate BMI"):
#         if weight <= 0 or height <= 0:
#             st.error("Please enter valid weight and height.")
#         else:
#             bmi = calculate_bmi(weight, height)
#             st.write(f"Your BMI is: {bmi:.2f}")
#             st.write(get_recommendations(bmi))

# # Main function to run the Streamlit app
# def main():
#     bmi_calculator()

# if __name__ == "__main__":
#     main()