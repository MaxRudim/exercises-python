import requests

try:
    requests.get('http://pudim.com.br/')

except Exception:
    print('Não consegui acessar o site do pudim :(')

else:
    print('Acessei o site do pudim :D')
