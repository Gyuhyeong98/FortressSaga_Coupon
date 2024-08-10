import streamlit as st
from streamlit_utils.submit import submit


def run():
    col1, col2 = st.columns(2)

    col1.subheader("쿠폰 입력")
    col1_event = col1.container()
    coupons = col1.text_area(
        "coupons",
        key="many_to_one_coupons",
        label_visibility="collapsed",
        height=150,
        placeholder="""쿠폰-1
    쿠폰-2
    ...
    쿠폰-000
    """,
    )

    col2.subheader("닉네임 입력")
    col2_event = col2.container()
    names = col2.text_input(
        "names",
        key="many_to_one_names",
        label_visibility="collapsed",
    )
    _, col, _ = st.columns(3)

    col_result = st.container()
    col_result.markdown("---")
    col_result.subheader("결과")

    col.button(
        "제출하기",
        on_click=submit,
        key="many_to_one_btn",
        kwargs={
            "fields": {
                "coupon": col1_event,
                "names": col2_event,
                "result": col_result,
            },
            "names": names,
            "coupon": coupons,
        },
        use_container_width=True,
    )
