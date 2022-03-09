def ajuda(com):
    help(com)


def título(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP!')
    comando = str(input('Função ou biblioteca (Digite fim para sair) >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO!')
