def verifica(num):
    teste = []
    cont = menor = maior = 0

    for a in num.split():
        teste.append(int(a))

    for c in teste:
        if cont == 0:
            maior = c
            menor = c
            cont += 1
        else:
            if maior < c:
                maior = c
            if menor > c:
                menor = c

    return f'{maior} {menor}'
#    return teste

print(verifica('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'), '542 -214')
print(verifica('1 2 3 4 5'))
print(verifica("1 2 -3 4 5")) # return "5 -3"
print(verifica("1 9 3 4 -5")) # return "9 -5"