from streamlit.delta_generator import DeltaGenerator
from coupon_api import fortress_saga_coupon


def submit(fields: dict[str, DeltaGenerator], names: str, coupon: str):
    if not names:
        fields["names"].error("닉네임을 입력해주세요")
    if not coupon:
        fields["coupon"].error("쿠폰을 입력해주세요")
    if names and coupon:
        names = [i.strip() for i in names.split("\n")]
        coupon = [i.strip() for i in coupon.split("\n")]
        result = fortress_saga_coupon(names=names, coupons=coupon)
        fields["result"].dataframe(
            result,
        )
