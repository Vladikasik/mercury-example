from urllib.parse import urlencode
import hashlib


# base_url = 'https://exchange.mercuryo.io/'
# widget_id = '27daec1a-932c-4543-a2b0-2ca4946cb590'
# params = {
#     "widget_id": widget_id,
#     "type": "buy",
#     "currency": "USDC",
#     "network": "SOLANA",
#     "amount": 30,
#     "fiat_currency": "EUR",
# }
# final_url = f"{base_url}?{urlencode(params)}"
# print(final_url)

###
address = 'Bsw8DaAn7tb7n4AuP1WWVDS4BjEW3EVKnDwobqx8WYFC'
secret = 'secret'
signature_input = f"{address}{secret}"
signature = hashlib.sha512(signature_input.encode()).hexdigest()

base_url = 'https://exchange.mercuryo.io/'
widget_id = '27daec1a-932c-4543-a2b0-2ca4946cb590'
params = {
    "widget_id": widget_id,
    "type": "buy",
    "currency": "USDC",
    "network": "SOLANA",
    "amount": 30,
    "fiat_currency": "EUR",
    "address": address,
    "signature": signature,
}
final_url = f"{base_url}?{urlencode(params)}"
print(final_url)