import requests
import json

from time import sleep


URL = "https://fortress-saga.bm.cookappsgames.com/coupon/use"
HEADER = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}

MSG = {
    "THE_PRODUCT_HAS_BEEN_SENT_TO_YOUR_MAILBOX": "보상 지급",
    "INVALID_NICKNAME": "유효하지 않은 닉네임",
    "INVALID_COUPON": "유효하지 않은 쿠폰",
    "THE_COUPON_REDEMPTION_PERIOD_HAS_ENDED": "쿠폰 사용 기간 종료",
    "THE_COUPON_HAS_ALREADY_BEEN_REDEEMED": "이미 지급된 쿠폰",
    "YOU_CANNOT_RECEIVE_DUPLICATE_REWARDS": "이미 지급된 쿠폰",
    "SERVER_ERROR_PLEASE_TRY_AGAIN": "서버 오류",
}


def response_parser(name: str, coupon: str, response: requests.request) -> dict:
    result = json.loads(response.text)
    result = MSG.get(result["msg"], "개발자에게 오류 내용을 보고해주세요.")
    result = {"name": name, "coupon": coupon, "result": result}
    return result


def fortress_saga_coupon(names: list[str], coupons: list[str]) -> list[dict]:
    results = []
    for coupon in coupons:
        for name in names:
            sleep(0.1)
            body = {"nickName": name, "code": coupon}
            response = requests.post(url=URL, headers=HEADER, json=body, timeout=3)
            results.append(response_parser(name=name, coupon=coupon, response=response))
    return results
