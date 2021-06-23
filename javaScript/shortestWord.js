//Simple, given a string of words, return the length of the shortest word(s).
//String will never be empty and you do not need to account for different data types.


function findShort(s){
    var lista = s.split(' '); //Transforma em lista como o teste.split() do python
    var menor;
    for(var i = 0; i < lista.length; i++){
        if(i == 0){
            menor = lista[i].length;
        }
        else if(menor > lista[i].length){
            menor = lista[i].length;
        }
    }
    return console.log(menor);
    
}

findShort("bitcoin take over the world maybe who knows perhaps");
findShort("turns out random test cases are easier than writing out basic ones"); 
findShort("Let's travel abroad shall we");