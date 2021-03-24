def high(x):
    p = x.lower().split() #pegar apenas minúsculas e separando as palavras.
    a = 'abcdefghijklmnopqrstuvwxyz'
    maior = 0
    
    for y in p: #varrer lista
        cont = 0
        for z in y: #varrer palavras(itens da lista)
            cont += a.find(z)+1 #conta as posições dos caracteres
        if cont > maior: #se for cont for maior que o último valor maior inserido.
            maior = cont
            nome = y #captura o nome da palavra
    return nome