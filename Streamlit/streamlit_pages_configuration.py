import streamlit as st

from PIL import Image

icon = Image.open('./favicon.png') #ico extnsion

st.set_page_config(
	page_title = 'Hello World!',
	page_icon = icon,
	layout = 'centered', #wide
	initial_sidebar_state = 'auto', #collapsed, expanded
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com',
		'About':'About your application: **Hello World!**'
	}
	)


st.sidebar.title("Hello World!")
st.title("Hello World!")


hide_footer_style = '''
<style>
.reportview-container .main footer {visibility: hidden;}
'''
st.markdown(hide_footer_style, unsafe_allow_html=True)


hide_menu_style = '''
<style>
#MainMenu {visibility: hidden;}
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)
