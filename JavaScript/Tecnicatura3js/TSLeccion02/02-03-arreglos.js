//Creacion de Array o arreglos
//let autos = new Array("Ferrari","Reno","BMW"); esta es la sintaxis vieja

const autos = ["Ferrari","Reno","BMW"];
console.log(autos);

//Recorrer los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++) {
    console.log(i+" : "+autos[i])
}

//Modificamos los elementos del arreglo
autos[1] = "Volvo"
console.log(autos[1])

//Agregamos nuevos valores al arreglo
autos.push("Audi"); //Agregamos el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = "Porche";
console.log(autos)

//Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = "camaro"
console.log(autos);

//Como preguntar sin es un Array o un Arreglo
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array

