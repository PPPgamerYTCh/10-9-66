import streamlit as st
import streamlit as st
from PIL import Image
import requests
password = "ผ่าน"
st.markdown("<h1 style='text-align: center;'>🧙‍♂️🪄 ห้องแห่งปริศนา 🌃🌌</h1>", unsafe_allow_html=True)


link = "https://drive.google.com/drive/folders/1BQ7uaohA7mtluKP45Gp_Us6As8qiStkO?usp=drive_link"
st.markdown(
    f"<div style='display: flex; justify-content: center;'><a href='{link}' style='text-align: center;'>🪄 ไปตามหากุญแจกันน 🗝️</a></div>",
    unsafe_allow_html=True,
)

# Add a text input widget for the password
entered_password = st.text_input("Enter the password:", type="password")

# Add an "Enter" button to submit the password
if st.button("Enter",use_container_width=True):
    if entered_password == password:
        st.balloons()
        st.markdown("<h1 style='text-align: center;'>🎂🎂🎈Happy Birth Day🥳🥳🎉</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'></h1>", unsafe_allow_html=True)
        st.markdown(
            """
                <div style="display:flex; justify-content:center; align-items:center;">
                <img src="https://drive.google.com/uc?id=1Hak-fzrOqXdYvBcqKK9VMS8tui3_sCbo" style="width:300px; height:200px; margin: 10px;">
                <img src="https://drive.google.com/uc?id=1W0ugJp_TTCtS8yve2tOeW9ndyt6wp_x8" style="width:300px; height:200px; margin: 10px;">
                <img src="https://drive.google.com/uc?id=1VcEIPskWcBiuVhOyy_zatE3redB1hQkV" style="width:300px; height:200px; margin: 10px;">
                </div>
            """, unsafe_allow_html=True)
        text = """
        สุขสันต์วันเกิดนะเพื่อน วันเกิดนายปีนี้เราขออวยพรแบบออนไลน์นะ ขอให้นายมีความสุขมาก ๆ สุขภาพร่างกายแข็งแรง อะไรไม่ดีขอให้ไม่เข้ามา พบเจอแต่สิ่งดี ๆ เรียนได้เกรด A ทุกวิชานะเพื่อน คิดถึงนายเสมอนะ ว่าง ๆ อยากไปเล่นด้วยอยู่ แฮป ๆ ครับเพื่อนสุดเลิฟฟ 💖💖
        """
        centered_text = f'<div style="display: flex; justify-content: center; align-items: center; height: 50vh;"><div style="text-align: center; font-size: 24px;">{text}</div></div>'
        st.markdown(centered_text, unsafe_allow_html=True)
        st.markdown(
            """
                <div style="display:flex; justify-content:center; align-items:center;">
                <img src="https://drive.google.com/uc?id=1hwgnfkiK-Pjue0daXb-0rnMU1Gvo-dFy" style="width:300px; height:200px; margin: 10px;">
                <img src="https://drive.google.com/uc?id=10HxEd5zoutoz1ngqAiOPvIT7KuoFSpCg" style="width:300px; height:200px; margin: 10px;">
                <img src="https://drive.google.com/uc?id=1OEABcNrpGW8rids52dnKc6k1_ePJeOeb" style="width:300px; height:200px; margin: 10px;">
                </div>
            """, unsafe_allow_html=True)