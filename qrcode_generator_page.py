import streamlit as st
import segno
import time

# page config
def generate_qrcode_page():

    st.image("https://i.pinimg.com/564x/aa/9a/a2/aa9aa2eb5165e676bd8e9b37be0ec1d0.jpg")

    st.title("QR Code Generator")

    url = st.text_input("Please enter the data you want to encode:")

    def generate_qrcode(url):
        qrcode = segno.make_qr(url)
        qrcode.to_pil(scale=10).save("qrcode_streamlit.png")

    if url:
        with st.spinner("Generate QR Code"):
            time.sleep(3)
        generate_qrcode(url)
        st.image("qrcode_streamlit.png",
                 caption="Here you go!"
                 )

        st.markdown("@spideym00n")