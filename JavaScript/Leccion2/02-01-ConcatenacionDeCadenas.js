/*var nombre = "Matias ";
var apellido = "Gomez";
var nombreComleto = nombre+" "+apellido; //Primera Concatenacion
console.log(nombreComleto);
var nombreCompleto2 = "Laura"+" "+"Altamirano"; //Segunda Concatenacion 
console.log(nombreCompleto2);
var juntos = nombre + 12; //Lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (22 + 12); // Aqui se puede diferenciar a travez de los parentesis
console.log(juntos)
juntos = 12 + 12 + nombre;
console.log(juntos)

let x, y;
x = 17, y = 21;
let z = x + y;
console.log(z);

let _1num = 20;
let rompie = "rompe todo";
console.log(_1num);
console.log(rompie);

//Al dia de la fecha la variable "Var" ya no se utiliza mas, se considera mala practica!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

let nombre2 = "Matias";
console.log(nombre2)

const apellido2 = "Gomez";
//apellido2 = "goma" una constante no puede ser modificada es un valor fijo (constante)
console.log(apellido2)
*/

//Ampliando el uso de var let y const, con var puedes reasignar en cualquier momento, este forma parte del ambito global, un error es que se sobreescriba

var nombre = "Ariel"
nombre = "Osvaldo"
console.log(nombre);

function saludar (){
    var nombr3 = "Laura"
    console.log(nombre3);
}

//console.log(nombre3) //Aqui no lee el dato en la funcion 

if(true){
    var edad = 34
    console.log(edad)
}

console.log (edad) //En la funcion funciona bien, en la estructura if fallo


/*
let: esta puerde ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar (){
    let nombre2 = "Ariel";
    console.log(nombre2)
}
//console.log(nombre2)

if(true){
    let edad2 = 33;
}
//console.log(edad2);

//const: se utiliza para valores constantes que no pueden ser reasignadas

const fechanacimiento = 2006;
console.log(fechanacimiento);
//fechanacimiento = 2003;
//console.log(fechanacimiento)
