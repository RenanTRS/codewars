def array_diff(a, b):
    diferenca = []
    for c in a:
        if c not in b: #Foi bem simples, bastou ver se c estava ou não na lista b
            diferenca.append(c) #pegava sempre os que não estavam
    
    return diferenca