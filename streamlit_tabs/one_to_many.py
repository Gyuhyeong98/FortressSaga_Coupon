import streamlit as st
from streamlit_utils.submit import submit


def run():
    col1, col2 = st.columns(2)

    col1.subheader("쿠폰 입력")
    col1_event = col1.container()
    coupon = col1.text_input(
        "coupon",
        key="one_to_many_coupon",
        label_visibility="collapsed",
    )

    col2.subheader("닉네임 입력")
    col2_event = col2.container()
    names = col2.text_area(
        "names",
        key="one_to_many_names",
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
        key="one_to_many_btn",
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
