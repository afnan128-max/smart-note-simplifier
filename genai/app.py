import streamlit as st
from utils.extract_text import extract_text_from_pdf
from utils.keyword_extractor import extract_keywords
from utils.formula_extractor import extract_formulas
from utils.simplifier import get_summary, simplify_text

st.set_page_config(page_title="Smart Note Simplifier", layout="centered")

st.title("🧠 Smart Note Simplifier & Formula Extractor")
st.caption("Upload your study notes, and get simplified summaries, keywords, and extracted formulas!")

uploaded_file = st.file_uploader("📄 Upload a PDF or TXT file", type=["pdf", "txt"])
kid_mode = st.checkbox("🧒 Simplify explanations to kid-level vocabulary")
from utils.sentiment import classify_sentiment

st.header("🧾 Sentiment Classifier")
user_review = st.text_area("Enter any paragraph or review you'd like to classify:")

if st.button("Classify Sentiment"):
    if user_review.strip() == "":
        st.warning("Please enter a review to classify.")
    else:
        with st.spinner("Analyzing..."):
            sentiment = classify_sentiment(user_review)
            st.success(f"🧠 Sentiment Detected: {sentiment}")


if uploaded_file:
    with st.spinner("Processing your notes..."):
        raw_text = extract_text_from_pdf(uploaded_file)

        st.subheader("📌 Extracted Keywords")
        keywords = extract_keywords(raw_text)
        st.write(keywords)

        st.subheader("🧮 Detected Formulas")
        formulas = extract_formulas(raw_text)
        st.write(formulas if formulas else "No formulas detected.")

        st.subheader("🧠 Short Notes Summary")
        summary = simplify_text(raw_text) if kid_mode else get_summary(raw_text)
        st.write(summary)
