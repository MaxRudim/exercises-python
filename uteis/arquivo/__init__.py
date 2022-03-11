from uteis import menu


def arquivoExiste(nome):

    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        #  O + significa que se o arquivo não está criado,
        #  é para o sistema criar.
        a.close()

    except Exception:
        print('Houve um erro na criação do arquivo')

    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):

    try:
        a = open(nome, 'rt', encoding='utf-8')

    except Exception:
        print(f'Erro ao ler o arquivo {nome}')

    else:
        menu.cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):

    try:
        a = open(arq, 'at')

    except Exception:
        print('Houve um erro na abertura do arquivo.')

    else:
        try:
            a.write(f'{nome};{idade}\n')

        except Exception:
            print('Houve um erro na hora de escrever os dados.')

        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
