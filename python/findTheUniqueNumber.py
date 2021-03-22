def find_uniq(arr):
    n = arr
    i = arr[0] #valor para comparação
    a = []
    b = []
    for x in n:
        if i == x:
            a.append(x)
        else:
            b.append(x)
    
    if len(a) < len(b): #Alimentei duas listas porém apensa um número é diferente logo a que tiver menos caracteres conterá a resposta certa
        n = a[0]
    else:
        n = b[0]
    return n   # n: unique integer in the array