#Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized 
#according to the given dimensions. **The return value of the function must be an array, and the numbers must be Fixnums, NOT 
#strings.Each value on the table should be equal to the value of multiplying the number in its first row times the number in its 
#first column.


def multiplication_table(row,col):
    # Good Luck!
    matriz = []
    linha = []
    for l in range(1, row+1):
        for c in range(1, col+1):
            linha.append(l * c)
        matriz.append(linha[:])
        linha.clear()
    return matriz

print(multiplication_table(2,2), [[1,2],[2,4]])
print(multiplication_table(3,3), [[1,2,3],[2,4,6],[3,6,9]])
print(multiplication_table(3,4), [[1,2,3,4],[2,4,6,8],[3,6,9,12]])
print(multiplication_table(4,4), [[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]])
print(multiplication_table(2,5), [[1,2,3,4,5],[2,4,6,8,10]])