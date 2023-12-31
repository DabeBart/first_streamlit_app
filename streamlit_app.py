import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError




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

fruit_choice = streamlit.text_input('What fruit would you like information about? ',"kiwi")
streamlit.write('The user entered ', fruit_choice)                                 

import requests
fruit_choice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#output it the screen as a table
import pandas
#streamlit.text(fruityviceresponse.jason())
#streamlit.dataframe(fruityvice_normalized)
streamlit.text(fruit_choice_response.json())
streamlit.dataframe(fruit_choice_response)


'''import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)'''



# this will not work correctly, but just go with it for the now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

'''#streamlit.text("fruit load list contains:")
#streamlit.text(my_data_row)
'''
'''#my_data_rows = my_cur.fetchone()'''



# allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit);
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('"jackfruit" + "papaya" + "guava" + "kiwi")")
        return "Thanks for adding " + new_fruit

# add a button to load the fruit
if streamlit.button ('Get Fruit List');
  my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

# don't run anything here while we troubleshoot
streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit load list contains:")
streamlit.dataframe(my_data_rows)
fruit_choice1 = streamlit.text_input('What fruit would you like to add? ','jackfruit')
streamlit.write('Thanks for Adding ', fruit_choice1)    

