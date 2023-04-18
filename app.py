import streamlit as st
from snscrape.modules.twitter import TwitterUserScraper
import pandas as pd
from Predict import *
from Scraper import *
from transformers import pipeline

# Model and pipeline
MODEL_PATH = 'danielcd99/multilanguage-toxicity-classifier'

def load_pipeline():
    pipe=pipeline(
    "text-classification",
    model=MODEL_PATH
    )
    return pipe

pipe = load_pipeline()


# Title and subtitle
st.title("Toxicity Detection")
st.subheader("This is an app for detecting toxicity in tweets written in portuguese. "
          "Write the name of the user (without @) and select the number of tweets you want to check.")


# User information
with st.form(key='forms'):
    st.markdown(
        """Insert the **twitter user** (sem o @) to receive a toxicity analysis of the last tweets. 
        \n#### Result are classified in:
- 0: Harmless
- 1: Toxic
        """)
    username = st.text_input(label='Username:')
    number_of_tweets = st.selectbox(
        'How many tweets do you want to check?',
        (5, 10, 20, 30))
    submit_button = st.form_submit_button(label='Analyze')

if submit_button:
    scraper = TwitterUserScraper(username)
    tweets = get_tweets(scraper, number_of_tweets)
    predictions = get_predictions(tweets, pipe)

    st.table(pd.DataFrame({'tweet': tweets, 'toxic':predictions}))