let x = 10;
console.log(x.length);
console.log("Tipos primitivos");

let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "nemesoldier@gmail.com",
    edad: 30,
    nombreCompleto: function(){ //metodo o funcion en JavaScript
        return this.nombre+" "+this.apellido;
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
