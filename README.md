<p align="center"><img width="500" src="./assets/slash.png"></p>

<a href="https://zenodo.org/doi/10.5281/zenodo.10023643"><img src="https://zenodo.org/badge/702291989.svg" alt="DOI"></a>
[![codecov](https://codecov.io/gh/SE23-Team44/slash-phase4/branch/main/graph/badge.svg?token=9YO9QKQZPJ)](https://codecov.io/gh/SE23-Team44/slash-phase4)
[![Build Status](https://app.travis-ci.com/rohan22shah/slash-phase3.svg?branch=main)](https://app.travis-ci.com/rohan22shah/slash-phase3)
[![Python Style Checker](https://github.com/SE23-Team44/slash-phase4/actions/workflows/style_checker.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/style_checker.yml)
[![Run Tests On Push](https://github.com/SE23-Team44/slash-phase4/actions/workflows/unit_test.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/unit_test.yml)
[![Python Application](https://github.com/SE23-Team44/slash-phase4/actions/workflows/python-app.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/python-app.yml)
[![Lint Python](https://github.com/SE23-Team44/slash-phase4/actions/workflows/main.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/main.yml)
[![Running Code Coverage](https://github.com/SE23-Team44/slash-phase4/actions/workflows/code_cov.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/code_cov.yml)
[![Close as a feature](https://github.com/SE23-Team44/slash-phase4/actions/workflows/close_as_a_feature.yml/badge.svg)](https://github.com/SE23-Team44/slash-phase4/actions/workflows/close_as_a_feature.yml)

<!--Badges-->
<a href="https://github.com/SE23-Team44/slash-phase4/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/SE23-Team44/slash-phase4"></a>
<a href="https://github.com/SE23-Team44/slash-phase4/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/SE23-Team44/slash-phase4"></a>
<a href="https://github.com/SE23-Team44/slash-phase4/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/SE23-Team44/slash-phase4"></a>
<a href="https://github.com/SE23-Team44/slash-phase4/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/SE23-Team44/slash-phase4"></a>
<img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/SE23-Team44/slash-phase4">
<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/SE23-Team44/slash-phase4">
<img alt="Discord Channel" src="https://img.shields.io/discord/1162231656980168876">


<p align="center">
    <a href="https://github.com/SE23-Team44/slash-phase4/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/SE23-Team44/slash-phase4/issues/new/choose">Request Feature</a>
</p>


Do you love shopping? Are you in search of some good deals while shopping online?! Slash is here to help you look for the best deals!


Slash is a publicly accessible web API framework that allows one to scrape the most popular e-commerce websites to get the best deals on the searched items across multiple e-commerce websites. Currently supported websites include [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), and [EBay](https://www.ebay.com/).
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash introduces easy to use public APIs to filter, sort and search through the search results
- **Powerful**: Produces JSON responses that can be easily customised to bring about the desired output

---

<p align="center">
  <a href="#movie_camera-checkout-our-video">Checkout our video</a>
  ::
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#computer-technology-used">Technology Used</a>
  ::
  <a href="#bulb-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#golf-future-roadmap">Future Roadmap</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  ::
  <a href="#Acknowledgement">Acknowledgement</a>
  ::
  <a href="#email-support">Support</a>
  
</p>

---

:movie_camera: Checkout our video
---

[![Video](https://img.youtube.com/vi/aGQisQmQt-o/0.jpg)](https://www.youtube.com/watch?v=aGQisQmQt-o)


---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/MeryHarikaG/slash-phase5.git
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
3. To run this project, you must install PostgreSQL on your system. If you haven't already installed it, you can download the latest version of PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/).

### Configuring Database Connection

Once you've installed PostgreSQL, follow these steps to set up the database connection in your project:

i. Open the database.py file in your project directory.

ii. Locate the top section of the code where you define the database connection settings. It might look something like this:

   ```
   username = 'postgres'
   password = 'pass'
   ```
Replace username and password value from 'postgres', 'pass' with your PostgreSQL username password, respectively.

4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```main.py``` file.
```
cd src

For Mac
python3 main.py

For Windows
python main.py
```
5. To run streamlit application
```
streamlit run slash_user_interface.py
```

:computer: Technology Used
---
- Streamlit [https://streamlit.io/]
- Fast API
- Postgre SQL
- Python

:bulb: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for students who wish to get the best deals out of every e-commerce site and can be used by anyone who is willing to develop an application that consumes these web APIs.
- Future scope includes anything from a web application with a frontend or any Android or IOS application that utilises these Web APIs at their backend. Anyone can build their own custom application on top of these web APIs.

:golf: Phase 4 developments
---
- Implemented secure user-based login with PostgreSQL and JWT, enhancing the project usability.
- Implemented the wishlist feature, making it easy for users to save and access search results.
- Significantly improved UI with sidebar, dedicated pages, and a robust wishlist feature.
- Added currency conversion, allowing users to view results in their preferred currency.
- Users can now download search results in CSV format, enhancing utility.
- Integrated a PostgreSQL database for login and wishlist functionalities.

<img src = https://github.com/SE23-Team44/slash-phase4/blob/main/assets/search%20gif.gif>

:golf: Future Roadmap
---
Future Roadmap

* Pagination Feature: Implement a pagination feature for the result table allowing to scrape and display multiple results from various e-commerce sites in an organized manner.

* UI Enhancement: Continue to enhance the user interface to provide an even better user experience. Consider improving aesthetics, user-friendliness, and overall design.

* Additional Account Settings: Introduce additional account settings to give users more control over their profiles and preferences, enhancing their personalization and usability.

* Predictive Model: Develop a predictive model that can determine the optimal timing for purchasing the least expensive product from the search results. This feature will provide valuable guidance to users, helping them make informed decisions.

* Enhanced Search Capabilities: Improve the search functionality by introducing advanced search capabilities. This can include options for filtering search results based on ratings, price ranges, and other relevant criteria, giving users more refined search options.

* Multi-Platform Integration: Expand the platform's capabilities by incorporating search results from various e-commerce platforms such as Etsy, Dick's Sporting Goods, and more. This will provide users with optimized outcomes from a diverse selection of online vendors.

* Highlight Cheapest Product: Highlight the most affordable product in the result table and display it separately for an easier user experience. This feature can help users quickly identify the best deals.

* Social Media Login: Add support for different methods of login, such as Gmail, Facebook, or other social media accounts, to provide users with convenient and secure login options.

* Price Chart Visualization: Introduce a visual representation of price trends for products. This feature can help users understand historical price changes and make more informed purchasing decisions.

* Wishlist Sharing: Enable users to share their wishlists with others. This collaborative feature can be useful for sharing gift ideas or getting recommendations from friends and family.


:sparkles: Contributors
---
<table>
  <tr>
    <td align="center"><a href="https://github.com/MeryHarikaG"><br/><sub><b>Mery Harika Gaddam</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kothasrilakshmi"><br /><sub><b>Sri Lakshmi Kotha</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/tbattul"><br/><sub><b>Tanmaiyee Reddy Battula</b></sub></a></td>
    <td align="center"><a href="https://github.com/kavyajoshi510"><br /><sub><b>Kavya Lalbahadur Joshi</b></sub></a><br /></td>
</tr>
</table>

## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of Maintaining a good Software Engineering project. We would also like to thank the teaching assistants for their support throughout the project.
We would also like to extend our gratitude to previous group : https://github.com/rohan22shah/slash-phase3
- [https://streamlit.io/](https://streamlit.io/)
- [https://shields.io/](https://shields.io/)

:email: Support
---
For any queries and help, please reach out to us at : simlyclipse43@gmail.com
