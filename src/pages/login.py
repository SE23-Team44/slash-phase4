"""
Copyright (c) 2023 Sharat Neppalli
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

import requests
import streamlit as st
from src.pages.wishlist import render_wishlist

def render_login():

    with open('assets/style.css') as f:
        st.markdown(f"""
            <style>
            {f.read()}
            </style>
        """, unsafe_allow_html=True)

    API_URL = "http://127.0.0.1:5050/auth"

    # Initialize session state variables
    st.session_state.token = st.session_state.get('token', None)
    st.session_state.cookie = st.session_state.get('cookie', None)

    placeholder = st.empty()
    if not st.session_state.token:
        placeholder.empty()
        with placeholder.container():
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login = st.button("Login")
            if login:
                if username and password:
                    response = requests.post(
                        f"{API_URL}/token",
                        data={"username": username, "password": password}
                    )
                    if response.json().get("user"):
                        st.session_state.token = response.json().get("user")
                        st.session_state.cookie = response.cookies.get("access_token")
                        st.write(f"You are now logged in {st.session_state.token}")
                        st.rerun()
                    else:
                        st.error("Login failed. Please check your credentials.")
                else:
                    st.warning("Please enter both username and password.")


