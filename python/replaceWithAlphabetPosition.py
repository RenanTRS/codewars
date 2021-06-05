#Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in 
#the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nuns = []
    for c in text:
        if c in alphabet:
            posicao = alphabet.find(c) + 1
            nuns.append(str(posicao))
    
    num = ' '.join(nuns)
    return num

print(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")