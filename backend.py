def calculate_bmi(weight, height):
    """
    Function to calculate BMI based on weight (in kg) and height (in meters).
    """
    bmi = weight / (height ** 2)
    return bmi

def get_recommendations(bmi):
    """
    Function to generate recommendations based on BMI.
    """
    if bmi < 18.5:
        return "You are underweight. Consider consuming more calories and protein-rich foods."
    elif 18.5 <= bmi < 25:
        return "You have a normal weight. Keep maintaining a balanced diet and regular exercise routine."
    elif 25 <= bmi < 30:
        return "You are overweight. Focus on portion control, increase physical activity, and consume more whole foods."
    else:
        return "You are obese. Consult a healthcare professional for personalized advice and focus on gradual weight loss through diet and exercise."

