import streamlit as st
from db import get_user
import bcrypt

st.title("🔑 Login")

if "email" in st.session_state:
    st.success(f"Already logged in as {st.session_state['email']}")
    if st.button("Logout"):
        del st.session_state["email"]
        st.info("You have been logged out.")
else:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(email)
        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
                st.session_state["email"] = user["email"]
                st.success(f"Welcome back, {user['username']}!")
            else:
                st.error("Invalid password")
        else:
            st.error("No account found with this email")
