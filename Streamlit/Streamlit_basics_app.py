# Core Pkg
import streamlit as st 

# TEXT
# title
st.title("Streamlit Basics")

# header/subheader
st.header("Text")
st.header("Text Dimension (This is a header)")

st.subheader("This is a subheader")

# text
st.text("This is a simple text")

# write
st.write("This is a write dimension")

# MARKDOWN
st.markdown("# This is markdown")

# Linkable Text and Links
st.header("Linkable Text and Links")
# Links
st.markdown("[Streamlit](https://www.streamlit.io/)")

url_link = "https://rosariomoscato.github.io/"

st.markdown(url_link)

# HTML (Style)
st.header("HTML (Style)")
#Custom Color/Style
html_page = """
<div style="background-color:blue;padding:50px">
	<p style="color:cyan;font-size:50px">Enjoy Streamlit!</p>
	
</div>
"""
st.markdown(html_page,unsafe_allow_html=True)


# HTML (Style)
st.header("Colors")
st.success("Success!")

st.info("Information")
st.warning("This is a warning")
st.error("This is an error")


# Images, Video and Audio
st.header("Images, Video and Audio")
# Images
from PIL import Image
img = Image.open("RML_Logo.png")
st.image(img,width=300,caption="My Image")

# Video
video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Video URL/YTB
st.video("https://www.youtube.com/watch?v=8YKYs2LIxHQ")

# Audio
audio_file = open('sample1.mp3',"rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes,format="audio/mp3")


st.header("Widgets")
st.button("Submit")

if st.button("Write"):
	st.text("Hello world")

# Checkbox
if st.checkbox("Checkbox"):
	st.success("Checkbox selected")

# Radio
radio_but = st.radio("Your Selection",["A","B"])

if radio_but == 'A':
	st.info("You selected A")
else:
	st.info("You selected B")

# Select
city = st.selectbox("Your City",["Napoli","Roma","Palermo","Catania"])


# Multiselect
occupation = st.multiselect("Your Occupation",["ML Engineer","Data Scientist","AI Consultant","Python Programmer"])


# TEXT INPUT
name = st.text_input("Your Name","Type Here")
st.text(name)

# NUMBER INPUT
age = st.number_input("Input a number")

# TEXT_AREA
message = st.text_area("Your Message","Type here")

# SLider
select_val = st.slider("Select a Value",1,10)

# Balloons
if st.button("Balloons"):
	st.balloons()



# Dataframes and Tables
st.header("Dataframes and Tables")
import pandas as pd 
df = pd.read_csv("auto.csv")

st.dataframe(df.head(10))

st.table(df.head(10))


# Plottings
st.header("Plottings")
import matplotlib.pyplot as plt 
import seaborn as sns 

# Area_chart
st.area_chart(df)
# Bar_chart
st.bar_chart(df.head(20))
# Line Chart
st.line_chart(df.head(10))

# Heatmap
fig, ax = plt.subplots()
corr_plot = sns.heatmap(df.corr(),annot=True)
st.pyplot(fig)


# Date & Time
st.header("Date & Time")
import datetime 
today = st.date_input("Today is",datetime.datetime.now())

import time
the_time = st.time_input("The time is",datetime.time(10,0))


# Display JSON,CODE
data = {"name":"John","surname":"Wick"}
st.json(data)

# Display Code
st.code("import pandas as pd")

st.code("import pandas as pd",language='python')

julia_code ="""
function doit(num::int)
	println(num)
end
"""

st.code(julia_code,language='julia')


# Progress Bar and Spinner
st.header("Progress Bar and Spinner")
# Progress Bar
# import time 
# my_bar = st.progress(0)
# for percent in range(100):
# 	time.sleep(0.1)
# 	my_bar.progress(percent+1)

# Spinner

# with st.spinner("Please wait..."):
# 	time.sleep(10)
# st.success("Done!")

