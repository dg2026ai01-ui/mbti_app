import streamlit as st

st.set_page_config(
    page_title="MBTI 청소년 도서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 청소년 문학 도서 추천")
st.subheader("✨ 당신의 MBTI에 맞는 책을 추천해 드립니다!")

st.write("MBTI 유형을 선택하면 청소년에게 어울리는 문학 도서를 추천해드려요 😊")

# MBTI 선택
mbti = st.selectbox(
    "🧠 당신의 MBTI를 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

# 추천 도서 데이터
books = {
    "INTJ": ("어린 왕자", "깊은 사고와 철학적 이야기를 좋아하는 INTJ에게 추천 🌌"),
    "INTP": ("멋진 신세계", "아이디어와 사고 실험을 좋아하는 INTP에게 추천 💡"),
    "ENTJ": ("데미안", "자기 성장과 리더십을 고민하는 ENTJ에게 추천 🔥"),
    "ENTP": ("허클베리 핀의 모험", "자유로운 모험을 좋아하는 ENTP에게 추천 🏕️"),

    "INFJ": ("연금술사", "자신의 꿈과 의미를 찾는 INFJ에게 추천 🌟"),
    "INFP": ("나미야 잡화점의 기적", "따뜻한 감성과 공감을 가진 INFP에게 추천 💌"),
    "ENFJ": ("죽은 시인의 사회", "사람들에게 영감을 주는 ENFJ에게 추천 🍎"),
    "ENFP": ("빨간 머리 앤", "상상력과 낭만이 가득한 ENFP에게 추천 🌸"),

    "ISTJ": ("동물 농장", "사회 구조와 질서를 생각하는 ISTJ에게 추천 🐷"),
    "ISFJ": ("작은 아씨들", "가족과 따뜻한 이야기를 좋아하는 ISFJ에게 추천 👨‍👩‍👧‍👦"),
    "ESTJ": ("페인트", "사회 규칙과 시스템을 생각하는 ESTJ에게 추천 🎨"),
    "ESFJ": ("Wonder", "친구와 공감의 이야기를 좋아하는 ESFJ에게 추천 🤝"),

    "ISTP": ("로빈슨 크루소", "생존과 모험 이야기를 좋아하는 ISTP에게 추천 🏝️"),
    "ISFP": ("모모", "감성과 예술적인 이야기를 좋아하는 ISFP에게 추천 ⏳"),
    "ESTP": ("80일간의 세계일주", "스릴과 모험을 좋아하는 ESTP에게 추천 🌍"),
    "ESFP": ("찰리와 초콜릿 공장", "즐거운 상상과 모험을 좋아하는 ESFP에게 추천 🍫")
}

# 추천 버튼
if st.button("📖 책 추천 받기"):
    title, desc = books[mbti]

    st.balloons()

    st.success(f"🎉 {mbti} 유형에게 추천하는 책!")

    st.markdown(f"""
    ## 📚 **{title}**

    {desc}

    좋은 독서 시간 보내세요! ✨📖
    """)

st.divider()

st.caption("💡 MBTI 기반 청소년 문학 추천 앱 | Streamlit")
