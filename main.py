import streamlit as st
st.title('나의 첫 웹서비스 만들기!❤')
name = st.text_input('이름을 입력해주세요.!')
menu = st.selectbox('좋아하는 음식을 선택해주세요!',['망고빙수','삼겹살구이','제육볶음','삼계탕'])
if st.button('인사말 생성하기') :
  st.write(name + '님! 당신이 좋아하는 음식은'+menu+'이군요! 저도 좋아요!')
