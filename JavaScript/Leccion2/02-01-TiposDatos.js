//Tipos de Datos
var nombre = "Matias"; //Tipo str
console.log (typeof nombre);
nombre = 7; 
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre)

var numero = 3000; //Tipo numerico
console.log (numero);

var objeto = {
    nombre :"Matias",
    apellido : "Gomez",
    telefono : "2634255267"
}
console.log (objeto);

//Tipo de dato Boolean
var bandera = true;
console.log(bandera);
//Tipo de dato funcion
function mifuncion(){}
console.log(typeof mifuncion);
//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);
//Tipo de dato Class
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre
        this.apellido = apellido
    }
}
console.log(typeof Persona)
//Tipo de dato undefined
var x;
console.log(typeof x)
//nul: Significa ausenscia de valor
var y = null; // null no es un tipo de dato, pero su origen es objet
console.log(typeof y);
x = undefined;
console.log(x);
//Tipo de datos array y Empty String
var autos = ["Audi","Ferrari","BMW"];
console.log(autos);
console.log(typeof autos);//Preguntamos que tipo de dato es:
var z = "";
console.log(z);
console.log(typeof z)


