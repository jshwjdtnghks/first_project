import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(page_title="가위✌️ 바위✊ 보🖐️ 게임", page_icon="🎮", layout="centered")

# 🌈 CSS 스타일 추가
st.markdown("""
    <style>
        body {
            background-color: #fceff9;
            color: #333333;
        }
        .title {
            font-size: 48px;
            text-align: center;
            color: #ff007f;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #7f00ff;
        }
        .emoji {
            font-size: 64px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🎮 제목
st.markdown('<div class="title">가위 ✌️ 바위 ✊ 보 🖐️ 게임 🎮</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">운을 시험해보세요! 컴퓨터를 이길 수 있을까요? 😎</div>', unsafe_allow_html=True)
st.markdown("---")

# 🧠 선택지
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐️": "paper"
}

# 🙋 사용자 선택
user_choice = st.radio("당신의 선택은?", list(choices.keys()), index=0)

# 🎲 컴퓨터 랜덤 선택
computer_choice = random.choice(list(choices.keys()))

# 🧾 결과 판단 함수
def determine_winner(user, computer):
    if user == computer:
        return "😐 비겼어요!"
    elif (user == "가위 ✌️" and computer == "보 🖐️") or \
         (user == "바위 ✊" and computer == "가위 ✌️") or \
         (user == "보 🖐️" and computer == "바위 ✊"):
        return "🎉 승리! 당신이 이겼어요!"
    else:
        return "😢 패배! 컴퓨터가 이겼어요!"

# 🎮 게임 시작 버튼
if st.button("결과 보기 🔍"):
    result = determine_winner(user_choice, computer_choice)

    st.markdown("## 당신의 선택 🎯")
    st.markdown(f'<div class="emoji">{user_choice}</div>', unsafe_allow_html=True)

    st.markdown("## 컴퓨터의 선택 💻")
    st.markdown(f'<div class="emoji">{computer_choice}</div>', unsafe_allow_html=True)

    st.markdown("## 결과 🎊")
    st.markdown(f"<h2 style='color: #ff4b4b; text-align:center;'>{result}</h2>", unsafe_allow_html=True)
