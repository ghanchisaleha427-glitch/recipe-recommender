import streamlit as st
from db import get_user_activity

st.title("📜 My Activity (History)")

user_email = st.session_state.get("email", None)

if user_email:
    activities = get_user_activity(user_email)
    if activities:
        st.markdown("### 🔥 Your Recipe History")
        for recipe_id, recipe_name, image_url, action, timestamp in activities:
            if image_url:
                st.image(image_url, width=200)
            st.subheader(recipe_name if recipe_name else "Unknown Recipe")
            st.write(f"📌 Action: {action}")
            st.write(f"🕒 {timestamp}")
            if recipe_id and recipe_id.strip():
                st.markdown(f"[View Again](Recipe_Detail?id={recipe_id})")
            st.markdown("---")
    else:
        st.info("No history yet.")
else:
    st.warning("Please login to view your history.")
