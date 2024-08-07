import streamlit as st
from coupon_api import fortress_saga_coupon


def submit(fields: list, names: str, coupon: str):
    if not names:
        fields["names"].error("닉네임을 입력해주세요")
    if not coupon:
        fields["coupon"].error("쿠폰을 입력해주세요")
    if names and coupon:
        names = [i.strip() for i in names.split("\n")]
        result = fortress_saga_coupon(names=names, coupon=coupon)
        fields["result"].dataframe(
            result,
        )


st.title("포트리스 사가")
st.subheader("쿠폰 자동 발송")
st.markdown("---")
col1, col2 = st.columns(2)

col1.subheader("쿠폰 입력")
col1_event = col1.container()
coupon = col1.text_input(
    "coupon",
    label_visibility="collapsed",
)

col2.subheader("닉네임 입력")
col2_event = col2.container()
names = col2.text_area(
    "names",
    height=150,
    label_visibility="collapsed",
    placeholder="""닉네임-1
닉네임-2
...
닉네임-000
""",
)
_, col, _ = st.columns(3)

col_result = st.container()
col_result.markdown("---")
col_result.subheader("결과")

col.button(
    "제출하기",
    on_click=submit,
    kwargs={
        "fields": {
            "coupon": col1_event,
            "names": col2_event,
            "result": col_result,
        },
        "names": names,
        "coupon": coupon,
    },
    use_container_width=True,
)
