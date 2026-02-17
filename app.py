# ----------------------------------------
# Streamlit + Hugging Face Sentiment App
# ----------------------------------------

import streamlit as st
from transformers import pipeline

# ----------------------------------------
# Page configuration
# ----------------------------------------
st.set_page_config(
    page_title="Movie Review Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# ----------------------------------------
# App title & description
# ----------------------------------------
st.title("🎬 Movie Review Sentiment Analyzer")

st.write(
    """
    This app analyzes **movie reviews** and predicts whether the sentiment is  
    **Positive 😊** or **Negative 😞** using a **pretrained Hugging Face NLP model**.

    ℹ️ The model is already trained on thousands of real movie reviews.
    """
)

st.markdown("---")

# ----------------------------------------
# Load pretrained sentiment model
# ----------------------------------------
# We use a fine-tuned model that already knows sentiment
# Hugging Face will download it automatically the first time
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

classifier = load_model()
st.write("MODEL LOADED:", classifier.model.config._name_or_path)

# ----------------------------------------
# User input section
# ----------------------------------------
st.subheader("📝 Enter Your Movie Review")

user_input = st.text_area(
    label="",
    placeholder="Example: The movie had brilliant acting and a powerful storyline.",
    height=160
)

# ----------------------------------------
# Analyze button
# ----------------------------------------
if st.button("🔍 Analyze Sentiment"):

    # Handle empty input
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a movie review before clicking analyze.")
    
    else:
        # Show spinner while model runs
        with st.spinner("Analyzing sentiment..."):
            result = classifier(user_input)[0]

        label = result["label"]
        confidence = result["score"]

        st.markdown("---")

        # ----------------------------------------
        # Handle low-confidence predictions
        # ----------------------------------------
        THRESHOLD = 0.60

        if confidence < THRESHOLD:
            st.warning(
                "🤔 The model is **not very confident** about this prediction.\n\n"
                "Try writing a longer or clearer review for better results."
            )

        # ----------------------------------------
        # Convert raw labels to user-friendly text
        # ----------------------------------------
        if label.upper() == "POSITIVE":
            st.success("### ✅ Sentiment: Positive 😊")
        else:
            st.error("### ❌ Sentiment: Negative 😞")


        # ----------------------------------------
        # Confidence display
        # ----------------------------------------
        st.write(f"**Confidence Score:** {confidence:.2f}")
        st.progress(confidence)

        st.caption(
            "Confidence shows how sure the model is about its prediction. "
            "Values closer to 1.0 indicate higher certainty."
        )

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("---")
st.caption(
    "Built using Hugging Face Transformers & Streamlit | Educational demo project"
)
