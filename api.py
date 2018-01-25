"""https://chain.so/api#code-examples"""

import requests
import json


def chain_get(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()  # 得到一个字典
        return content['data']


def pretty_print(parsed):
    print(json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    BTC_URL = {
        "get_price": "https://chain.so/api/v2/get_price/BTC/USD",
        "get_block": "https://chain.so/api/v2/get_block/BTC/200000",
        "get_tx": (lambda trx_id: f"https://chain.so/api/v2/get_tx/BTC/{trx_id}")
    }

    pretty_print(chain_get(BTC_URL["get_block"]))

    trx_id = "07809808a8528d75c4b89b80464fbfb90bf203a77cf4bfdf3ccb5a40a94f64c0"
    pretty_print(chain_get(BTC_URL['get_tx'](trx_id)))



