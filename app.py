import streamlit as st
from transformers import pipeline

# Title
st.title("📰 Deep Learning NLP App")
st.write("Prediksi Kategori Teks Berita")

# Load model (pakai model publik dulu biar pasti jalan)
classifier = pipeline("text-classification")

# Input teks
text = st.text_area("Masukkan teks:")

# Tombol prediksi
if st.button("Prediksi"):
    if text.strip() != "":
        result = classifier(text)
        st.success(f"Hasil prediksi: {result[0]['label']}")
    else:
        st.warning("Masukkan teks dulu!")
