from uteis import menu
from uteis import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = menu.menu(['Ver pessoas cadastradas.',
                         'Cadastrar nova pessoa.', 'Sair do Sistema'])

    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        menu.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = menu.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        menu.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
