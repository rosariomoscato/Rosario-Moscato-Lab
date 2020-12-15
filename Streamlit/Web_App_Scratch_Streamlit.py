"""
Created on Wed Dec 09 11:01:09 2020

@author: Rosario Moscato

Required Packages: streamlit textblob spacy gensim neattext matplotlib wordcloud 
Spacy Model: python -m spacy download en_core_web_sm
"""

# Core Pkgs
import streamlit as st 
st.set_page_config(page_title="NLP Simple Examples", page_icon="RML_Logo.png", layout='centered', initial_sidebar_state='auto')



# NLP Pkgs
from textblob import TextBlob 
import spacy
from gensim.summarization import summarize
import neattext as nt


# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


# Function For Tokens and Lemma Analysis
@st.cache
def text_analyzer(my_text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(my_text)
    allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
    return allData




# Function For Wordcloud Plotting
def plot_wordcloud(my_text):
    mywordcloud = WordCloud().generate(my_text)
    fig = plt.figure(figsize=(20,10))
    plt.imshow(mywordcloud,interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)




def main():
    """NLP App with Streamlit and TextBlob"""

    #st.title("NLP Simple Examples")

    title_templ = """
    <div style="background-color:blue;padding:8px;">
    <h1 style="color:cyan">NLP Simple Examples</h1>
    </div>
    """

    st.markdown(title_templ,unsafe_allow_html=True)

    subheader_templ = """
    <div style="background-color:cyan;padding:8px;">
    <h3 style="color:blue">Natural Language Processing On the Go...</h3>
    </div>
    """

    st.markdown(subheader_templ,unsafe_allow_html=True)

    st.sidebar.image("https://www.centreofexcellence.com/app/uploads/2016/09/nlp-diploma-course.jpg", use_column_width=True)

    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu",activity)



	# Text Analysis CHOICE
    if choice == 'Text Analysis':

        st.subheader("Text Analysis")        
        st.write("")
        st.write("")

        raw_text = st.text_area("Write something","Enter a Text in English...",height=250)

        if st.button("Analyze"):
            if len(raw_text) == 0:
            	st.warning("Enter a Text...")
            else:
            	blob = TextBlob(raw_text)
            	st.write("")

            	if blob.detect_language() != 'en':
            		st.warning("Enter a Text in English...")
            	else:
            		st.info("Basic Functions")
            		col1, col2 = st.beta_columns(2)

            		with col1:
            			with st.beta_expander("Basic Info"):
            				st.success("Text Stats")
            				word_desc = nt.TextFrame(raw_text).word_stats()
            				result_desc = {"Length of Text":word_desc['Length of Text'],
											"Num of Vowels":word_desc['Num of Vowels'],
											"Num of Consonants":word_desc['Num of Consonants'],
											"Num of Stopwords":word_desc['Num of Stopwords']}
            				st.write(result_desc)

            			with st.beta_expander("Stopwords"):
            				st.success("Stop Words List")
            				stop_w = nt.TextExtractor(raw_text).extract_stopwords()
            				st.error(stop_w)

            		with col2:
            			with st.beta_expander("Processed Text"):
            				st.success("Stopwords Excluded Text")
            				processed_text = str(nt.TextFrame(raw_text).remove_stopwords())
            				st.write(processed_text)

            			with st.beta_expander("Plot Wordcloud"):
            			    st.success("Wordcloud")
            			    plot_wordcloud(raw_text)



            		st.write("")
            		st.write("")
            		st.info("Advanced Features")
            		col3, col4 = st.beta_columns(2)

            		with col3:
            			with st.beta_expander("Tokens&Lemmas"):
            				st.write("T&L")
            				processed_text_mid = str(nt.TextFrame(raw_text).remove_stopwords())
            				processed_text_mid = str(nt.TextFrame(processed_text_mid).remove_puncts())
            				processed_text_fin = str(nt.TextFrame(processed_text_mid).remove_special_characters())
            				tandl = text_analyzer(processed_text_fin)
            				st.json(tandl)

            		with col4:
            			with st.beta_expander("Summarize"):
            				st.success("Summarize")
            				summary_text = summarize(raw_text,ratio=0.4)
            				if summary_text != "":
            					st.success(summary_text)
            				else:
            					st.warning("Please insert a Longer Text")


        


    # Translation CHOICE
    elif choice == 'Translation':

        st.subheader("Text Translation")

        st.write("")
        st.write("")
        raw_text = st.text_area("","Write something to be translated...")
        if len(raw_text) < 3:
            st.warning("Please provide a string with at least 3 characters...")
        else:
            blob = TextBlob(raw_text)
            lang = blob.detect_language()
            #st.write(lang)
            tran_options = st.selectbox("Select translation language",['Chinese', 'English', 'German', 'Italian', 'Russian', 'Spanish'])
            if st.button("Translate"):
                if tran_options == 'Italian' and lang != 'it':
                    st.text("Translating to Italian...")
                    tran_result = blob.translate(from_lang=lang, to='it')
                elif tran_options == 'Spanish' and lang != 'es':
                    st.text("Translating to Spanish...")
                    tran_result = blob.translate(from_lang=lang, to='es')
                elif tran_options == 'Chinese' and lang != 'zh-CN':
                    st.text("Translating to Chinese...")
                    tran_result = blob.translate(from_lang=lang, to='zh-CN')
                elif tran_options == 'Russian' and lang != 'ru':
                    st.text("Translating to Russian...")
                    tran_result = blob.translate(from_lang=lang, to='ru')
                elif tran_options == 'German' and lang != 'de':
                    st.text("Translating to German...")
                    tran_result = blob.translate(from_lang=lang, to='de')
                elif tran_options == 'English' and lang != 'en':
                    st.text("Translating to English...")
                    tran_result = blob.translate(from_lang=lang, to='en')
                else:
                    tran_result = "Text is already in " + "'" + lang + "'"


                st.success(tran_result)
            
        
    

    # Sentiment Analysis CHOICE
    elif choice == 'Sentiment Analysis':
        
        st.subheader("Sentiment Analysis")

        st.write("")
        st.write("")

        raw_text = st.text_area("", "Enter a Text...")

        if st.button("Evaluate"):
            if len(raw_text) == 0:
                st.warning("Enter a Text...")
            else:
                blob = TextBlob(raw_text)
                lang = blob.detect_language()

                if lang != 'en':
                    tran_result = blob.translate(from_lang=lang, to='en')
                    blob = TextBlob(str(tran_result))

                result_sentiment = blob.sentiment
                st.info("Sentiment Polarity: {}".format(result_sentiment.polarity))
                st.info("Sentiment Subjectivity: {}".format(result_sentiment.subjectivity))

        



    # About CHOICE
    else:# choice == 'About':
        st.subheader("About")

        st.write("")
        st.write("")

        st.markdown("""
        ### NLP Simple Examples (App with Streamlit and TextBlob)
        
        ##### By
        + **[Rosario Moscato LAB](https://www.youtube.com/channel/UCDn-FahQNJQOekLrOcR7-7Q)**
        + [rosariomoscatolab@gmail.com](mailto:rosariomoscatolab@gmail.com)
        """)






if __name__ == '__main__':
	main()
