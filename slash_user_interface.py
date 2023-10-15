import sys
sys.path.append('../')
import pandas as pd
import streamlit as st
from src.main_streamlit import search_items_API
from src.url_shortener import shorten_url
import re
import requests
import webbrowser

def extract_and_format_numbers(input_string):
    # Use regular expressions to find all numbers in the input string
    numbers = re.findall(r'\d+\.\d+|\d+', input_string)

    if len(numbers) >= 2:
        # Take the first number and add a decimal point before the second number
        formatted_output = '$'+ numbers[0] + '.' + numbers[1]
        return formatted_output
    elif len(numbers) == 1:
        # If there's only one number, return it as is
        return '$'+ numbers[0]
    else:
        return "No valid numbers found in the input."



def ensure_https_link(link_text):
    if link_text.startswith("http://") or link_text.startswith("https://"):
        return link_text
    else:
        return "https://" + link_text
        
def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'

def path_to_url_html(path):
    return '<a href="'+ ensure_https_link(path) +'" target="_blank">Product Link</a>'

@st.cache
def convert_df_to_html(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html,Link=path_to_url_html))

@st.cache
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

st.set_page_config(page_title="Slash - Product Search", page_icon="🔍")

# Load external CSS for styling
with open('assets/style.css') as f:
    st.markdown(f"""
        <style>
        {f.read()}
        </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------

# variable to store if the user is logged in
token = None
API_URL = "http://127.0.0.1:5050/auth"
BASE_URL = "http://localhost:8501"


# signin = st.button("Sign In", key = "signin")

if not token and st.button("Register", key = "register"):
     webbrowser.open_new_tab(f"{API_URL}/register")

if not token:# and signin:
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
                if response.json():
                    token = response.json()
                    st.write("You are now logged in.")
                else:
                    st.error("Login failed. Please check your credentials.")
            else:
                st.warning("Please enter both username and password.")

if token:
    # User is logged in
    if st.button("View Wishlist"):
        wishlist_response = requests.get(f"{BASE_URL}/wishlist")
        if wishlist_response.status_code == 200:
            st.write(wishlist_response.json()["message"])
        else:
            st.error("Failed to retrieve wishlist.")
    if st.button("Logout"):
        response = requests.get(f"{API_URL}/logout")
        token = None
        st.success("Logged out successfully.")
        st.markdown(
        """
        <script>
        window.location.reload();
        </script>
        """,
        unsafe_allow_html=True
        )


# -----------------------------------------------------------------------

# Display Image
st.image("assets/slash.png")

# Create a two-column layout
col1, col2,col3 = st.columns(3)

# Input Controls
with col1:
    product = st.text_input('Enter the product item name')

with col2:
    website = st.selectbox('Select the website', ('Walmart', 'Ebay', 'BestBuy', 'Target', 'All'))

with col3:
    button = st.button('Search')

website_dict = {
    'Amazon': 'az',
    'Walmart': 'wm',
    'Ebay': 'eb',
    'BestBuy': 'bb',
    'Target': 'tg',
    'Costco': 'cc',
    'All': 'all'
}

# Search button
if button and product and website:
    results = search_items_API(website_dict[website], product)
    # Use st.columns based on return values
    description = []
    url = []
    price = []
    site = []
    image_url = []

    if results:
        for result in results:
            if result != {} and result['price'] != '':
                description.append(result['title'])
                url.append(result['link'])
                site.append(result['website'])
                price.append(extract_and_format_numbers(result['price']))
                image_url.append(result['img_link'])
    if len(price):
        
        def highlight_row(dataframe):
            df = dataframe.copy()
            minimumPrice = df['Price'].min()
            mask = df['Price'] == minimumPrice
            df.loc[mask, :] = 'background-color: lightgreen'
            df.loc[~mask, :] = 'background-color: ""'
            return df
        dataframe = pd.DataFrame({'Description': description, 'Price': price, 'Link': url, 'Website': site, 'Image':image_url})
        st.balloons()
        st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>RESULT</h1>", unsafe_allow_html=True)

        html = "<div class='table-container'>"
        html += convert_df_to_html(dataframe)
        st.markdown(
            html,
            unsafe_allow_html=True
        )
        html += '</div>'
        csv = convert_df_to_csv(dataframe)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='output.csv',
            mime='text/csv',
        )

        st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>Visit the Website</h1>", unsafe_allow_html=True)
        min_value = min(price)
        min_idx = [i for i, x in enumerate(price) if x == min_value]
        for minimum_i in min_idx:
            link_button_url = shorten_url(url[minimum_i].split('\\')[-1])
            st.write("Cheapest Product [link](" + link_button_url + ")")
    else:
        st.error('Sorry, the website does not have similar products')


# Footer
footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0%;
width: 100%;
background-color: #DFFFFA;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/sathiya06/slash-phase3" target="_blank">slash</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/anshulp2912/slash/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 Rohan Shah</a></p>
<p>Contributors: Aadithya, Dhiraj, Sathya, Sharat</p>
</div>
"""
# st.markdown(footer, unsafe_allow_html=True)
