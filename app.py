import streamlit as st
import streamlit_tabs

st.title("포트리스 사가")
st.subheader("쿠폰 자동 발송")
tab1, tab2 = st.tabs(
    [
        "👥 쿠폰 여러명 사용",
        "📜 쿠폰 여러개 사용",
    ]
)

with tab1:
    streamlit_tabs.one_to_many.run()

with tab2:
    streamlit_tabs.many_to_one.run()
