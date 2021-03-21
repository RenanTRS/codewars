def find_short(s):
    l = len(s)
    a = s.split()
    for x in a:
        if l > len(x):
            l = len(x)
        
    return l # l: shortest word length