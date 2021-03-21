def find_short(s):
    l = len(s) #conta a quantidade caracteres apenas para ter um número alto o suficiente para comparação.
    a = s.split() #separa as palavras
    
    for x in a:
        if l > len(x): #se l for maior que a quantidade de letras na palavra x, desse jeito l vai receber o valor menor sempre
            l = len(x)
        
    return l # l: shortest word length