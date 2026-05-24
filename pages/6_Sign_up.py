import streamlit as st
from db import add_user
from email_service import send_otp

st.title("📝 Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if username and email and password:
        otp = send_otp(email)
        st.session_state.otp = otp
        st.session_state.username = username
        st.session_state.email = email
        st.session_state.password = password
        st.success("OTP sent to your email. Please verify below.")

if "otp" in st.session_state:
    user_otp = st.text_input("Enter OTP sent to your email:")
    if st.button("Verify OTP"):
        if user_otp == st.session_state.otp:
            add_user(st.session_state.username, st.session_state.email, st.session_state.password)
            st.success("Account created and verified successfully!")
            st.session_state.clear()
        else:
            st.error("Invalid OTP")
