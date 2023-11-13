import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header(':bowl_with_spoon: Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text(':chicken: Hard-Boiled Free-Range Egg')
streamlit.text(':avocado: Avocado Toast')

streamlit.header(':banana: :strawberry: Build Your Own Fruit Smoothie 	:kiwifruit: :grapes:')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# pre-populated list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


import requests
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")

