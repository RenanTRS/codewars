/*Implement a function that adds two numbers together and returns their sum in binary. The conversion
can be done before, or after the addition. The binary number returned should be a string.*/


function addBinary(a,b) {
    var soma = a + b;
    var listaResto = [];
    var resto;
    var numBin = '';
    while(soma > 0){
        resto = Math.floor(soma % 2);
        listaResto.push(resto);
        soma = Math.floor(soma / 2);
    }

    while(listaResto.length > 0){
        numBin += listaResto.pop().toString();
    }
    
    return numBin;
}

console.log(addBinary(1, 1));