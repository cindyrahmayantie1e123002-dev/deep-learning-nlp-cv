import streamlit as st

st.title("Deep Learning NLP App")
st.write("Aplikasi berhasil jalan 🎉")

teks = st.text_input("Masukkan teks:")

if st.button("Prediksi"):
    st.success("Model siap! (nanti disambung ke model kamu)")
