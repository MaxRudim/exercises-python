def escreva(msg):
    len_msg = len(msg) + 4
    print('-' * len_msg)
    print(f'  {msg}')
    print('-' * len_msg)


msg = input('Escreva uma mensagem: ')
escreva(msg)
