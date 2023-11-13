import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header(':bowl_with_spoon: Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')

streamlit.header(':banana: :strawberry: Build Your Own Fruit Smoothie 	:kiwifruit: :grapes:')

import streamlit
import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
# pre-populated list
#fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index)['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(my_fruit_list )

import streamlit
streamlit.header('Fruityvice Fruit Advice!')
import requests
  #fruityvice_response = requests.get('https://fruityvice.com/api/fruit/kiwi')
  #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)                                 

import requests
fruit_choice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choic)

#output it the screen as a table
#streamlit.text(fruityviceresponse.jason())
#streamlit.dataframe(fruityvice_normalized)
streamlit.dataframe(fruit_choice_response)


