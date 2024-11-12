import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from qrcode_generator_page import generate_qrcode_page

st.set_page_config(page_title="QR Code App",
                   page_icon="<3")


options = ["Create QR Code", "Decodes QR Code", "About Me"]
page_selection = st.sidebar.selectbox("Menu",
                                      options)

if page_selection == "Create QR Code":
    generate_qrcode_page()
elif page_selection == "Decodes QR Code":
    decode_qrcode_page()
elif page_selection == "About Me":
    st.write("Hi, my name is Sarah!!!")
    st.image("https://i.pinimg.com/564x/14/9b/3f/149b3f0ec32d51dd17caff72f0dc9f96.jpg")