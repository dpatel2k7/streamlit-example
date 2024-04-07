import streamlit as st


def calculate_bmi(weight, height):
    """
    Function to calculate BMI based on weight (in kg) and height (in meters).
    """
    bmi = weight / (height ** 2)
    return bmi

def get_recommendations(bmi, name, age, days_active):

    if bmi < 18.5:
        st.write(f"Hello {name}, you are {age} years old and you stay active {days_active} days per week.")
        st.write("According to BMI, you are <span style='font-size:20px;color:red'><strong>underweight</strong></span>. Consider consuming more calories and protein-rich foods.</span>.", unsafe_allow_html=True)
        st.image("Underweight.png", use_column_width=True)
        st.write("We recommand you follow the meal plan suggested below.</span>", unsafe_allow_html=True)
        st.write("""
            | Day          | Meal 1                                                | Meal 2                                             | Meal 3                                               | Exercise                                             |
            |--------------|-------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
            | Monday       | Whole grain toast with nut butter (fiber, protein)    | Avocado and black bean wrap (fiber, healthy fats)   | Grilled chicken with quinoa and vegetables (protein, fiber) | 30-minute strength training (push-ups, squats, lunges) |
            | Tuesday      | Greek yogurt with granola and berries (protein, fiber) | Tuna salad on whole wheat pita (protein, fiber)    | Lentil soup with whole grain bread (fiber, protein)  | 20-minute jog or run                                |
            | Wednesday    | Smoothie with spinach, banana, and protein (fiber, protein) | Hummus and vegetable wrap (fiber, protein)      | Grilled salmon with sweet potatoes (protein, fiber) | 30-minute yoga session                              |
            | Thursday     | Scrambled eggs with avocado (protein, healthy fats)    | Quinoa and black bean salad (protein, fiber)      | Baked chicken with brown rice and vegetables (protein, fiber) | 20-minute home workout (jumping jacks, high knees) |
            | Friday       | Whole grain cereal with milk and fruits (fiber, vitamins) | Turkey and vegetable stir-fry (protein, fiber)  | Lentil curry with brown rice (fiber, protein)       | 30-minute bike ride                                 |
            | Saturday     | Cottage cheese with honey and nuts (protein, healthy fats) | Grilled vegetable and feta salad (fiber, protein) | Baked cod with quinoa and broccoli (protein, fiber) | 20-minute swim or water aerobics                   |
            | Sunday       | Pancakes with Greek yogurt and fruit (fiber, protein)  | Lentil soup with whole grain bread (fiber, protein) | Stir-fried tofu with vegetables and brown rice (protein, fiber) | Rest day                                             |""")
        st.write("If you have dietary restrictions check this [link](https://acl.gov/sites/default/files/nutrition/FoodSubstitutionList.pdf) out for a government approved list of substitutions.")

    elif 18.5 <= bmi < 25:
        st.write(f"Hello {name}, you are {age} years old and you stay active {days_active} days per week.")
        st.write("According to BMI, you have a <span style='font-size:20px;color:green'><strong>normal weight</strong></span>. Keep maintaining a balanced diet and regular exercise routine.</span>.", unsafe_allow_html=True)
        st.image("Normal.png", use_column_width=True)
        st.write("We recommand you follow the meal plan suggested below.</span>", unsafe_allow_html=True)
        st.write("""            
            | Day          | Meal 1                                                | Meal 2                                             | Meal 3                                               | Exercise                                             |
            |--------------|-------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
            | Monday       | Scrambled eggs with whole grain toast (protein, fiber) | Grilled chicken salad (protein, vegetables)         | Baked salmon with quinoa and vegetables (protein, fiber) | 30-minute brisk walk                                 |
            | Tuesday      | Greek yogurt with honey and almonds (protein, healthy fats) | Turkey and avocado wrap (protein, healthy fats) | Lentil soup with whole grain bread (fiber, protein)  | 20-minute home workout (push-ups, squats)           |
            | Wednesday    | Oatmeal with fruits and nuts (fiber, vitamins)         | Grilled vegetable and hummus wrap (fiber, protein) | Grilled chicken with sweet potatoes (protein, fiber) | 30-minute bike ride                                 |
            | Thursday     | Smoothie with spinach, banana, and protein (fiber, protein) | Tuna salad on whole grain bread (protein, fiber) | Grilled vegetables with brown rice (fiber, vitamins) | 20-minute jog or run                                |
            | Friday       | Whole grain pancakes with berries (fiber, vitamins)     | Turkey and vegetable stir-fry (protein, fiber)     | Baked cod with quinoa and broccoli (protein, fiber) | 30-minute yoga session                              |
            | Saturday     | Cottage cheese with pineapple (protein, vitamins)       | Grilled chicken Caesar salad (protein, vegetables) | Lentil chili with whole grain bread (protein, fiber) | 20-minute home workout (jumping jacks, lunges)     |
            | Sunday       | Whole grain toast with avocado and eggs (protein, fiber) | Quinoa and black bean salad (protein, fiber)      | Grilled salmon with asparagus and brown rice (protein, fiber) | Rest day                                             |""")
        st.write("If you have dietary restrictions check this [link](https://acl.gov/sites/default/files/nutrition/FoodSubstitutionList.pdf) out for a government approved list of substitutions.")

    elif 25 <= bmi < 30:
        st.write(f"Hello {name}, you are {age} years old and you stay active {days_active} days per week.")
        st.write("According to BMI, you are <span style='font-size:20px;color:red'><strong>overweight</strong></span>. Focus on portion control, increase physical activity, and consume more whole foods with high protien.</span>.", unsafe_allow_html=True)
        st.image("Overweight.png", use_column_width=True)
        st.write("We recommand you follow the meal plan suggested below.</span>", unsafe_allow_html=True)
        st.write("""
            | Day          | Meal 1                                                | Meal 2                                             | Meal 3                                               | Exercise                                             |
            |--------------|-------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
            | Monday       | Greek yogurt with honey and nuts (protein, healthy fats) | Grilled chicken salad (protein, vegetables)         | Baked salmon with quinoa and vegetables (protein, fiber) | 30-minute brisk walk                                |
            | Tuesday      | Whole grain toast with avocado (fiber, healthy fats)  | Turkey and vegetable wrap (protein, fiber)         | Lentil soup with whole grain bread (fiber, protein)  | 20-minute home workout (push-ups, squats)           |
            | Wednesday    | Oatmeal with fruits and nuts (fiber, vitamins)       | Grilled vegetable sandwich (fiber, vitamins)        | Grilled chicken with sweet potatoes (protein, fiber) | 30-minute bike ride                                 |
            | Thursday     | Smoothie with spinach, banana, and protein (fiber, protein) | Tuna salad on whole wheat crackers (protein, fiber) | Grilled vegetables with brown rice (fiber, vitamins) | 20-minute strength training (lunges, planks)        |
            | Friday       | Scrambled eggs with vegetables (protein, fiber)       | Hummus and veggie wrap (fiber, protein)            | Baked cod with quinoa and broccoli (protein, fiber) | 30-minute swim or water aerobics                    |
            | Saturday     | Cottage cheese with berries (protein, fiber)          | Grilled chicken Caesar salad (protein, vegetables)  | Turkey chili with whole grain bread (protein, fiber) | 20-minute yoga session                              |
            | Sunday       | Whole grain pancakes with fruit (fiber, vitamins)     | Grilled vegetable stir-fry (fiber, vitamins)        | Lentil curry with brown rice (fiber, protein)       | Rest day                                             |""")
        st.write("If you have dietary restrictions check this [link](https://acl.gov/sites/default/files/nutrition/FoodSubstitutionList.pdf) out for a government approved list of substitutions.")
    
    else:
        st.write(f"Hello {name}, you are {age} years old and you stay active {days_active} days per week.")
        st.write("According to BMI, you are <span style='font-size:20px;color:red'><strong>obese</strong></span>. Focus on maintaining a caloric deficiet to achieve gradual weight loss through diet and exercise</span>.", unsafe_allow_html=True)
        st.image("ObesePic.png", use_column_width=True)
        st.write("We recommand you follow the meal plan suggested below.</span>", unsafe_allow_html=True)
        st.write("""
            | Day          | Meal 1                                                | Meal 2                                             | Meal 3                                               | Exercise                                             |
            |--------------|-------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
            | Monday       | Oatmeal with fruits and nuts (fiber, vitamins)       | Grilled chicken salad (protein, vegetables)         | Baked salmon with quinoa and vegetables (protein, fiber) | 30-minute walk or jog                                |
            | Tuesday      | Greek yogurt with honey and nuts (protein, healthy fats) | Turkey and vegetable wrap (protein, vegetables)    | Lentil soup with whole grain bread (fiber, protein)  | 20-minute swim or water aerobics                     |
            | Wednesday    | Whole grain cereal with milk (fiber, protein)         | Grilled vegetable sandwich (fiber, vitamins)        | Grilled chicken with sweet potatoes (protein, fiber) | 30-minute bike ride                                 |
            | Thursday     | Smoothie with spinach, banana, and protein (fiber, protein) | Tuna salad on whole wheat crackers (protein, fiber) | Grilled vegetables with brown rice (fiber, vitamins) | 20-minute strength training (push-ups, squats)      |
            | Friday       | Scrambled eggs with vegetables (protein, fiber)       | Hummus and veggie wrap (fiber, protein)            | Baked cod with quinoa and broccoli (protein, fiber) | 30-minute strength training with light weights                                |
            | Saturday     | Cottage cheese with berries (protein, fiber)          | Grilled chicken Caesar salad (protein, vegetables)  | Turkey chili with whole grain bread (protein, fiber) | 20-minute yoga session                              |
            | Sunday       | Whole grain pancakes with fruit (fiber, vitamins)     | Grilled vegetable stir-fry (fiber, vitamins)        | Lentil curry with brown rice (fiber, protein)       | Rest day                                             |""")
        st.write("If you have dietary restrictions check this [link](https://acl.gov/sites/default/files/nutrition/FoodSubstitutionList.pdf) out for a government approved list of substitutions.")

