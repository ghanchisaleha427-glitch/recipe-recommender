import streamlit as st
from mealdb_api import get_meal_details
from db import log_activity

st.title("📖 Recipe Details")

# ✅ Correct way for new Streamlit
recipe_id = st.query_params.get("id")

user_email = st.session_state.get("email", "guest")

if recipe_id:
    meal = get_meal_details(recipe_id)
    if meal:
        st.subheader(meal["strMeal"])
        st.image(meal["strMealThumb"], width=400)

        st.write("📖 Category:", meal.get("strCategory", "N/A"))
        st.write("🌍 Cuisine:", meal.get("strArea", "N/A"))
        st.write("👩‍🍳 Instructions:", meal.get("strInstructions", "N/A"))

        st.markdown("### 🛒 Ingredients")
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                st.write(f"- {ingredient} ({measure})")

        # Log detail view
        log_activity(user_email, recipe_id, meal["strMeal"], meal["strMealThumb"], "detail_opened")

        # Feedback section
        st.markdown("---")
        st.markdown("### ⭐ Feedback")
        rating = st.radio("How would you rate this recipe?", [1, 2, 3, 4, 5], horizontal=True)
        if st.button("Submit Rating"):
            log_activity(user_email, recipe_id, meal["strMeal"], meal["strMealThumb"], f"rated_{rating}")
            st.success(f"Thank you! You rated this recipe {'⭐' * rating}")
    else:
        st.warning("No details found for this recipe.")
else:
    st.warning("No recipe ID provided.")
