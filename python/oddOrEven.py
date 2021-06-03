#Given a list of integers, determine whether the sum of its elements is odd or even. 
#Give your answer as a string matching "odd" or "even".
#If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr=0):
    pass
    soma = 0
    for c in arr:
        soma += c

    if soma % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(odd_or_even([0, 1, 2]), "odd")
print(odd_or_even([0, 1, 3]), "even")
print(odd_or_even([1023, 1, 2]), "even")
print(odd_or_even(), "even")