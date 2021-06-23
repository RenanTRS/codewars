//You get an array of numbers, return the sum of all of the positives ones.
//Note: if there is nothing to sum, the sum is default to 0.

function positiveSum(arr) {
    var num = arr;
    var soma = 0;
    for(var teste in num){
      if(num[teste] > 0){
        soma += num[teste];
      }
    }
    return console.log(soma);
}

positiveSum([1,-4,7,12]);