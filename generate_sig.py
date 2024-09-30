import hashlib
s_input = 'Bsw8DaAn7tb7n4AuP1WWVDS4BjEW3EVKnDwobqx8WYFC' + 'secret'
signature = hashlib.sha512(s_input.encode()).hexdigest()
print(signature)