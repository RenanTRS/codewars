def reverse_words(text):
    if '  ' in text: #Uma das strings possuía dois espaços para cada palavra, então usei estacondição.
        lista = text.split()
        novaLista = []
        for c in lista:
            novaLista.append(c[::-1]) #Varre a lista e me retorna os itens revertidos
        lista = '  '.join(novaLista) #Uso para juntar porém com dois espaços vazios de intervalo para cada item
        return lista
    else:
        lista = text.split()
        novaLista = []
        for c in lista:
            novaLista.append(c[::-1])
        lista = ' '.join(novaLista) #Juntar itens com apenas um espaço vazio entre eles.
        return lista