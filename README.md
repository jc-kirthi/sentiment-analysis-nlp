# 🎬 Movie Review Sentiment Analyzer (NLP App)

## 📌 Project Overview
This project is a Natural Language Processing (NLP) web application that analyzes movie reviews
and predicts whether the sentiment is **Positive 😊** or **Negative 😞**.

The application uses a **pretrained Hugging Face Transformer model** and is built with **Streamlit**
to demonstrate real-time NLP inference without training a model from scratch.

---

## 🧠 Problem Statement
To build an end-to-end NLP application that:
- Accepts human-written movie reviews
- Predicts sentiment accurately
- Clearly communicates prediction confidence
- Handles model uncertainty in a user-friendly way

---

## 🤗 Model Used
- **Model Name:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Type:** Pretrained & fine-tuned Transformer (SST-2)
- **Task:** Sentiment Analysis (Positive / Negative)

The model is already trained on a large movie-review sentiment dataset, making it suitable
for production-style inference without additional fine-tuning.

---

## 🛠️ Technologies Used
- Python  
- Hugging Face 🤗 Transformers  
- Streamlit  
- PyTorch  
- Google Colab (experimentation & learning)  
- VS Code  
- Git & GitHub  

---

## 🌐 Application Features
- Real-time sentiment prediction for movie reviews
- Human-readable sentiment output (no raw labels)
- Confidence score with visual progress bar
- Low-confidence warning for ambiguous reviews
- Clean and intuitive user interface
- Efficient model loading using Streamlit caching

---

## 📂 Project Structure
sentiment-analysis-nlp/

├── app.py # Streamlit web application

├── requirements.txt # Project dependencies

├── HuggingFace_Sentiment_Analysis.ipynb # Colab notebook (learning & experimentation)

└── README.md # Project documentation

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/sentiment-analysis-nlp.git
cd sentiment-analysis-nlp
```
```
pip install -r requirements.txt
streamlit run app.py
http://localhost:8501
```

### Deployment Note
This app requires Python 3.10 due to current Hugging Face Transformers compatibility.
Streamlit Cloud is configured using `runtime.txt` to ensure a stable runtime environment.


## ⚠️ Challenges Faced & Fixes

- Initially used a **base transformer model**, which produced incorrect sentiment predictions  
- Learned the difference between **base models** and **fine-tuned task-specific models**  
- Faced misleading predictions due to **label mismatch** (`LABEL_1` vs `POSITIVE`)  
- Resolved the issue by **inspecting raw model outputs** and updating label handling logic  
- Understood how **Streamlit caching** can affect ML model loading during development  

---

## ✅ Key Learnings

- Pretrained models are commonly used in **real-world NLP applications**  
- Fine-tuning is **not mandatory** for every use case  
- Model outputs must be **interpreted carefully** in application logic  
- Confidence scores help **communicate uncertainty** to users  
- Debugging ML apps often involves **environment and runtime inspection**  

---

## 🚀 Future Improvements

- Fine-tune a custom sentiment model on **domain-specific data**  
- Add **prediction history** and basic analytics  
- Support **multilingual sentiment analysis**  
- Deploy the app on **Streamlit Community Cloud**  
