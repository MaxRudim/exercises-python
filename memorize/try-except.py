#  Estrutura do try, except, else e finally.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b

except Exception as erro:
    # Evite usar apenas except.
    # Se o except for genérico, use except Exception.
    # É possível renomear Exception para pegar o erro.
    # É possível ter diversos Exception para qualquer tipo de exceção.
    print(f'ERRO: O erro encontrado foi: {erro.__class__}')

else:
    # Quando coloca o else a mensagem de erro do terminal some.
    # Acontece quando o resultado dá certo.
    print(f'O resultado é {r:.1f}')

finally:
    # Acontece independentemente se deu certo ou se deu erro.
    # O else e o finally são opcionais.
    print('Volte sempre, muito obrigado!')
