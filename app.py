import streamlit as st

# Title of the app
st.title("Calorie Tracker")

# Dropdown for selecting a food item
food_items = {
    "Apple": 52,  # Calories per 100g
    "Banana": 89,
    "Chicken Breast": 165,
    "Rice": 130,
    "Pizza": 266,
    "Burger": 295,
    "Salad": 30
}

food_choice = st.selectbox("Select a food item:", list(food_items.keys()))

# Input field for quantity in grams
quantity = st.number_input("Enter quantity (grams):", min_value=1, value=100)

# Calculate total calories
if st.button("Calculate Calories"):
    total_calories = (food_items[food_choice] / 100) * quantity
    st.success(f"Total Calories for {quantity}g of {food_choice}: {total_calories:.2f} kcal")

# Reliable image URL from Unsplash
image_url = "https://images.unsplash.com/photo-1512621776951-a57141f2eefd"
st.image(image_url, caption="Healthy Food Choices", use_container_width=True)
