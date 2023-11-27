from pyclbr import Function
from src.pages.search import render_search
from src.pages.wishlist import render_wishlist
from src.pages.login import render_login
from src.pages.register import render_register
from src.pages.logout import render_logout

import streamlit as st

st.set_page_config(page_title="Slash - Product Search", page_icon="🔍")
st.markdown("<span class='float-box'><h1 class='float'>Slash - Product Search</h1></span>", unsafe_allow_html=True)
st.session_state.token = st.session_state.get("token", None)

class UIManager:
    def __init__(self):
        self.pages = []

    def addPage(self, title, render_method):
        self.pages.append({"title": title, "function": render_method})

    def render(self):
        st.sidebar.markdown("## Main Menu")
        page = st.sidebar.selectbox(
            "Select Page", self.pages, format_func=lambda page: page["title"]
        )
        page["function"]()


uiManager = UIManager()

uiManager.addPage("Search", render_search)
if st.session_state.token:
    uiManager.addPage("Wishlist", render_wishlist)
    uiManager.addPage("logout", render_logout)
else:
    uiManager.addPage("Login", render_login)
    uiManager.addPage("Register", render_register)
uiManager.render()
