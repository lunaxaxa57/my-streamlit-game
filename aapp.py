import streamlit as st

characters = {
    "إيلان": "الطيبة، تحب السلام، وتفكر قبل لا تتكلم.",
    "نورة": "الذكية، دايم عندها خطة، وتفكر بسرعة.",
    "صبا": "الهادية، بس إذا لعبت صارت قوية فجأة.",
    "تولين": "الغامضة، شخصيتها ما تنفهم بسرعة.",
    "يارا": "المرحة، تحب تضحك وتخلي الجو حلو.",
    "رنيم": "الجادة، تركّز وتفكر بذكاء هجومي."
}

st.set_page_config(page_title="لعبة التحدي", page_icon="🎮", layout="centered")
st.markdown("<h1 style='text-align: center; color: pink;'>اختار شخصيتك 💫</h1>", unsafe_allow_html=True)

selected = st.selectbox("اختر شخصيتك:", list(characters.keys()))
st.write("✨ الوصف:")
st.success(characters[selected])

opponent = st.selectbox("اختر الخصم:", [c for c in characters if c != selected])

if st.button("ابدأ التحدي!"):
    st.markdown(f"🔥 <h3>{selected} تواجه {opponent}!</h3>", unsafe_allow_html=True)
    st.balloons()
https://sh
