"""
Copyright (c) 2023 Mery Harika Gaddam
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""
import streamlit as st
import re
import json
import requests
import pandas as pd
from src.url_shortener import shorten_url

def extract_and_format_numbers(input_string):
    # Use regular expressions to find all numbers in the input string
    numbers = re.findall(r'\d+\.\d+|\d+', input_string)

    if len(numbers) == 4:
        # Place dots between numbers
        formatted_output = '$'+ numbers[0] + '.' + numbers[1]+'.'+numbers[2]+'.'+numbers[3]
        return formatted_output
    elif len(numbers) == 3:
        # Place dots between numbers
        formatted_output = '$'+ numbers[0] + '.' + numbers[1]+'.'+numbers[2]
        return formatted_output
    elif len(numbers) == 2:
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

@st.cache_data
def convert_df_to_html(input_df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html,Link=path_to_url_html))

def render_wishlist():
    # Check if the user is logged in and if 'cookie' is initialized
    if 'token' not in st.session_state or not st.session_state.token or 'cookie' not in st.session_state:
        st.warning("Login first to add item into wishlist.")
        return  # Return early from the function

    API_URL = "http://127.0.0.1:5050"

    # Load external CSS for styling
    with open('assets/style.css') as f:
        st.markdown(f"""
            <style>
            {f.read()}
            </style>
        """, unsafe_allow_html=True)

    # To get all the products wishlisted by the user
    # Make sure 'cookie' is available before making the request
    if 'cookie' in st.session_state and st.session_state.cookie:
        response = requests.get(
            f"{API_URL}/wishlist",
            cookies={"access_token": st.session_state.cookie}
        )
        response_json = response.json()  # This converts the response to a Python dictionary
    else:
        st.warning("You need to log in to see your wishlist.")
        return

    list = []

    for key, value in response_json.items():
        product = json.loads(value)
        product['product_id'] = key
        list.append(product)

    description = []
    url = []
    price = []
    site = []
    image_url = []
    product_id = []

    list.sort(key=lambda x: (float(x['product_id'])),reverse=True)

    for result in list:
        description.append(result['Description'])
        url.append(result['Link'])
        site.append(result['Website'])
        price.append(extract_and_format_numbers(result['Price']))
        image_url.append(result['Image'])
        product_id.append(result['product_id'])

    dataframe = pd.DataFrame({'product_id':product_id, 'Description': description, 'Price': price, 'Link': url, 'Website': site, 'Image':image_url})
    st.markdown("<div class='neon'><h2>Wish List</h2></div>", unsafe_allow_html=True)
    st.write("[Most recently added product link](" + shorten_url(list[0]['Link'].split('\\')[-1]) + ")")
    st.write("Most recently added item is displayed first")


    html = "<div class='table-container'>"
    html += convert_df_to_html(dataframe)
    st.markdown(
        html,
        unsafe_allow_html=True
    )
    html += '</div>'

    st.write("\n")
    st.write("Enter the Product.Id. of the item to delete it from the wishlist.")
    product_index = st.text_input('Delete From Wish List')
    wishlist_button = st.button('Delete')
    if wishlist_button:
        # Again, make sure 'cookie' is available before making the request
        if 'cookie' in st.session_state and st.session_state.cookie:
            response = requests.delete(
                f"{API_URL}/wishlist/{product_index}",
                cookies={"access_token": st.session_state.cookie}
            )

            if response.status_code == 200:
                st.write("Removed successfully")
                st.rerun()
        else:
            st.warning("You need to log in to modify your wishlist.")

