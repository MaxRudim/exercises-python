print('\033[1;31;107mOlá mundo\033[m')

# text                    background

# 30      black           preto       40
# 31      red             vermelho    41
# 32      green           verde       42
# 33      yellow          amarelo     43
# 34      blue            azul        44
# 35      Magenta         Magenta     45
# 36      cyan            ciano       46
# 37      grey            cinza       47
# 97      white           branco      107

# sem nada: \033[m
# padrão: \033[style;text;backgroundm
# m deve sempre estar no final.
# style pode ser: 0(normal), 1(negrito); 4(sublinhado)
# ou 7(cor e background invertido)

# Para tirar as formatações que se extendem, digite após a frase: \033[m
