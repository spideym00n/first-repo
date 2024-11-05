import streamlit as st
import segno
import time

# page config

st.set_page_config(
    page_title="My QR Code Generator",
    page_icon="<3"
)

st.image("https://i.pinimg.com/564x/c4/d2/e7/c4d2e77654582fc58dcddb7882a26647.jpg")

st.title("QR Code Generator")

url = st.text_input("Please enter the data you want to encode:")

def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10).save("images/qrcode_streamlit.png")

if url:
    with st.spinner("Generate QR Code"):
        time.sleep(3)
    generate_qrcode(url)
    st.image("images/qrcode_streamlit.png",
             caption="Here you go!"
             )

    st.markdown("@spideymoon")