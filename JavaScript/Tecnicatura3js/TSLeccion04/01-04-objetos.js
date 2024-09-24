let x = 10;
console.log(x.length);
console.log("Tipos primitivos");

let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "nemesoldier@gmail.com",
    edad: 28,
    idioma: "es",
    get lang(){
        return this.idioma.toUpperCase(); //Comvierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //metodo o funcion en JavaScript
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return "El nombre es: " +this.nombre+", Edad: "+this.edad;
    }
}

console.log(persona.nombre); 
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona)
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto")

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14"
persona2.telefono = "542634255267"
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto")
console.log(persona["apellido"]);  //Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in")
//For in y accedemos al objeto como si fuera un arreglo
for (propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad])
}
console.log("Cambiamos y eliminamos un error")
persona.apellida = "Betancud;"//Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla : concatenar cada valor de cada propiedad
console.log("Distinta formas de imprimir un objeto forma 1")
console.log(persona.nombre+", "+persona.apellido)
//Numero 2: a traves del ciclo for in
console.log("Distinta formas de imprimir un objeto forma 2")
for (nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
//Numero 3 La funcion object.values()
console.log("Distinta formas de imprimir un objeto forma 3")
let personaArray = Object.values(persona)
console.log(personaArray);

//numero 4: Utilizaremos el motodo JSON.stringify
console.log("Distinta formas de imprimir un objeto forma 4")
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad)

console.log("Comenzamos con el metodo get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

function persona3(nombre, apellido, email){ //Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new persona3("Leo","Lopez","lopeoz@gmail.com")
padre.nombre = "Luis" //Modificamos el nombre
padre.telefono = "54261786543";  //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion
let madre = new persona3("Laura","Contreras","contrara@laura.com");
console.log(madre)
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());
//Diferentes formas de crear objetos
//Caso objeto 1
let miObjeto = new Object();
//Caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada
//Caso String 1
let miCaddena1 = new String("Hola");
//Caso string 2
let miCaddena2 = "Hola" //Esta es la sintaxis simplificada y recomendada
// Caso con numeros 1
let miNumero = new Number(1); //Es formal no recomndable
//Caso con numeros 2
let miNumero2 = 1;

//Caso boolean 1
let miBoolean1 = new Boolean(false);
//Caso boolean 2
let miBoolean2 = false;   //Sintaxis recomendada

//Caso arreglos 1
let miArreglo1 = new Array(); //forma 1
//Caso arreglo 2
let miArreglo2 = []; //Sitaxis recomendada

//Caso function 1
let miFuncion1 = new function(){}  //Todo despues de new es considerado objeto
//Caso function 2
let miFuncion2 = function (){} //Notacion simplificada y recomendada

//Uso de prototype
persona3.prototype.telefono = "2612356434323";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "543234543342"
console.log(madre.telefono)

//Uso de call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
        //return this.nombre+" "+this.apellido;
    }
}

let persona5 = {
    nombre: "Carlos",
    apellido: "Lara"
}

console.log(persona4.nombreCompleto2("lic.","542323123534"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.","26342323123"));

//Metodo apply
let arreglo = ["Ing","542313123123"]
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));

