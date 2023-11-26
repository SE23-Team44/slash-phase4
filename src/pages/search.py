from locale import currency
import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
from src.main_streamlit import currency_API, search_items_API
from src.url_shortener import shorten_url
import re
import requests

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

@st.cache_data
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def render_search():
    def callback():
        st.session_state.button_clicked = True 

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    API_URL = "http://127.0.0.1:5050"
    
    # Load external CSS for styling
    with open('assets/style.css') as f:
        st.markdown(f"""
            <style>
            {f.read()}
            </style>
        """, unsafe_allow_html=True)

    # Display Image
    # st.image("assets/slash.png")

    # Create a three-column layout
    col1, col2, col3 = st.columns(3)

    # Input Controls
    with col1:
        product = st.text_input('Enter the product item name')

    with col2:
        website = st.selectbox('Select the website', ('Walmart', 'Ebay', 'BestBuy', 'Target', 'All'))
        button = st.button('Search', on_click=callback)

    with col3:
        currency = st.selectbox('Choose a currency', ('USD($)', 'EUR(€)', 'JPY(¥)', 'INR(₹)', 'GBP(£)', 'AUD($)', 'CAD($)'))
        Min_price = st.number_input('Minimum price', min_value=0, value=0)
        Max_price = st.number_input('Maximum price', min_value=0, value=10000)

    website_dict = {
        # 'Amazon': 'az',
        'Walmart': 'wm',
        'Ebay': 'eb',
        'BestBuy': 'bb',
        'Target': 'tg',
        # 'Costco': 'cc',
        'All': 'all'
    }

    add = False
    # Search button
    if (button or st.session_state.button_clicked ) and product and website and currency:
        results = search_items_API(website_dict[website], product)
        add = True
        # Use st.columns based on return values
        description = []
        url = []
        price = []
        site = []
        image_url = []
        
        for result in results:
            result['price'] = re.sub(r'\.(?=.*\.)', "", extract_and_format_numbers(result['price']).replace(extract_and_format_numbers(result['price'])[0], "", 1))

        results.sort(key=lambda x: (float(x['price'])))        

        if results:
            for result in results:
                if result != {} and result['price'] != '' and float(result['price'])>=Min_price and float(result['price'])<=Max_price:
                    description.append(result['title'])
                    url.append(result['link'])
                    site.append(result['website'])
                    price.append(extract_and_format_numbers(result['price']))
                    image_url.append(result['img_link'])

        if len(price):
            # def highlight_row(dataframe):
            #     df = dataframe.copy()
            #     minimumPrice = df['Price'].min()
            #     mask = df['Price'] == minimumPrice
            #     df.loc[mask, :] = 'background-color: lightgreen'
            #     df.loc[~mask, :] = 'background-color: ""'
            #     return df
            if(currency != "USD($)"):
                price = currency_API(currency, price)
            dataframe = pd.DataFrame({'Description': description, 'Price': price, 'Link': url, 'Website': site, 'Image':image_url})
            st.success(' Displaying \"'+ product +'\" from \"'+ website +'\" with price range - ['+str(Min_price)+', '+str(Max_price)+ ']'+' in \"'+ currency+'\"', icon="✅")
            st.markdown("<div class='neon'><h2>RESULTS</h2></div>", unsafe_allow_html=True)

            # min_value = min(price)
            # min_idx = [i for i, x in enumerate(price) if x == min_value]
            # for minimum_i in min_idx:
            #     link_button_url = shorten_url(url[minimum_i].split('\\')[-1])
            
            st.write("[Cheapest product link](" + shorten_url(results[0]['link'].split('\\')[-1]) + ")")
            st.write("Items are displayed in the increasing order of their prices")

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

        else:
            st.error('Sorry, the website does not have similar products')
    
    if (button or st.session_state.button_clicked ) and add:
        st.markdown("<h1 style='text-align: center; color: #1DC5A9;'>RESULT</h1>", unsafe_allow_html=True)

        # Display the product list and add-to-wishlist form
        product_index = st.text_input('Add To Wish List')
        with st.form(key='wishlist_form'):
            if st.form_submit_button('Add'):
                if product_index:
                    try:
                        product_index = int(product_index)
                        if 0 <= product_index < len(dataframe):
                            response = requests.post(
                                f"{API_URL}/wishlist",
                                data={"product_info": dataframe.iloc[product_index].to_json()},
                                cookies={"access_token": st.session_state.cookie}
                            )
                            if response:
                                st.write("Added successfully to the wishlist")
                        else:
                            st.error("Invalid product index")
                    except ValueError:
                        st.error("Invalid product index")

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
