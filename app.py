import streamlit as st
import torch
from summarizer.bert import Summarizer

# Summarization function using BERT-based summarizer


def summarize_text(text, num_sentences=5):
    model = Summarizer()
    summarized_text = model(text, num_sentences=num_sentences)
    return summarized_text


# Streamlit app layout
st.title("Content Summarizer")

# Textbox for content to be summarized
user_input_text = st.text_area("Enter the content you want to summarize:")

# Slider to select the number of sentences in the summary
num_sentences = st.slider("Number of summary sentences:", min_value=1, max_value=10)

# Button to trigger summarization
if st.button('Summarize'):
    # Check if there is text input
    if user_input_text:
        # Use num_sentences as the max_length parameter
        summarized_content = summarize_text(user_input_text, num_sentences)
        st.subheader("Summary")
        st.write(summarized_content)
    else:
        st.warning("Please enter some content to summarize.")
