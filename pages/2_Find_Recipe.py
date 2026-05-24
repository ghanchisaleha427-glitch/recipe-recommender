import streamlit as st
from mealdb_api import search_meal
from db import log_activity

st.title("🔍 Find Recipe")

user_email = st.session_state.get("email", "guest")
query = st.text_input("Enter ingredient or recipe name:")

if st.button("Search"):
    meals = search_meal(query)
    if meals:
        log_activity(user_email, None, query, None, "searched")
        for meal in meals:
            st.subheader(meal["strMeal"])
            st.image(meal["strMealThumb"], width=250)
            recipe_id = meal["idMeal"]
            # ✅ Use markdown link (works in all versions)
            st.markdown(f"[View Details](Recipe_Detail?id={recipe_id})")
    else:
        st.warning("No recipes found.")
