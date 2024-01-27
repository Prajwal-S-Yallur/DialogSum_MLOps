import streamlit as st
import requests

st.title('Sentiment Analysis')

text = st.text_input('Enter some text')

if st.button('Hit me'):

    payload = {'input_sentence': text}
    # payload = {'input_sentence': "I love this movie and i would watch it again and again!"}
    # # payload = {'input_sentence': "I like this movie, However its good to watch one time only."}
    # # payload = {'input_sentence': "I don't like this movie, as it had bad plot and bad acting."}
    url = 'http://127.0.0.1:8080/get_sentiment'

    result = requests.post(url, data=payload)

    # st.write(result.text)
    # st.write("Hi Uniphore!", text)
    st.json(result.text)