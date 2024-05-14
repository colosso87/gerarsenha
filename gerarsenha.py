#maiúsculas e minúsculas
#símbolos e espaços

"""
Security = chave
5ecurt1ty = senha

hex

1 = 1
2 = 2
até 9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F

"""

chave = input ("Digite a base da sua senha: ")

senha = ""
for letras in chave:
    if letra in "Aa": senha = senha + "10"
    elif letras in "Bb": senha = senha + "11"
    elif letras in "Cc": senha = senha + "12"
    elif letras in "Dd": senha = senha + "13"
    elif letras in "Ee": senha = senha + "14"
    elif letras in "Ff": senha = senha + "15"
    elif letras in "Rr": senha = senha + "#"
    elif letras in "Ss": senha = senha + "%"
    elif letras in "Mm": senha = senha + "$"
    elif letras in "Uu": senha = senha + "@"
    elif letras in "Gg": senha = senha + "*"
    else: senha = senha + letras
print(senha)             