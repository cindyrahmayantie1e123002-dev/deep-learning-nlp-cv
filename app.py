import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="NLP Text Classification",
    page_icon="🧠",
    layout="centered"
)

# ===== CSS WARNA BIRU =====
st.markdown("""
<style>
.main {
    background-color: #f5f9ff;
}
h1, h2, h3 {
    color: #0b5ed7;
}
.stButton>button {
    background-color: #0b5ed7;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton>button:hover {
    background-color: #084298;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.title("🧠 Aplikasi Klasifikasi Teks Berita")
st.write("Project Deep Learning - NLP")
st.divider()

st.markdown("""
Aplikasi ini menggunakan **Deep Learning Transformer**
untuk memprediksi kategori dari teks berita.
""")

st.subheader("✍️ Masukkan Teks Berita")

# ===== LOAD MODEL =====
@st.cache_resource
def load_model():
    return pipeline("text-classification")

model = load_model()

# ===== INPUT =====
text = st.text_area(
    "Tulis teks berita di sini:",
    height=150,
    placeholder="Contoh: Pemerintah mengumumkan kebijakan baru di bidang ekonomi..."
)

# ===== BUTTON =====
if st.button("🔍 Prediksi Kategori"):
    if text.strip() == "":
        st.warning("⚠️ Silakan masukkan teks terlebih dahulu.")
    else:
        with st.spinner("Model sedang menganalisis..."):
            result = model(text)

        st.success("Prediksi berhasil!")
        st.subheader("📊 Hasil Prediksi")
        st.info(result[0]["label"])

st.divider()
st.caption("© Project Deep Learning NLP 2026")
