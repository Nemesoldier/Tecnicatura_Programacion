let x = 10;
console.log(x.length);

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

let persona2 = new Object