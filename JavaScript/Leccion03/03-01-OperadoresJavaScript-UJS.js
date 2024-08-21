//Ejercicio para encontrar numeros pares
let parImpar = 3;
if (parImpar % 2 == 0){
    console.log("Es un numero PAR");
}
else {
    console.log("Es un numero IMPAR");
}


//Ejercicio es mayor de edad
let edad = 17, adulto = 18;
if (edad >= adulto){
    console.log("Es mayor de edad");
}
else{
    console.log("Es menor de edad");
}

//Ejercicio dentro de un rango
let dentroRango = 11;
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango")
}
else{
    console.log("Esta fuera del rango")
}

//Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("No puede asistir al juego de su hijo")
}

//Operador Ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 8
resultado2 = numero % 2 == 0 ? "Es un numero par" : "Es un numero impar"
console.log(resultado2)

//Convertir string a number
let miNumero = 18; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); // Esta es una funcion
console.log(typeof edad2);

//Funcion isnan 
if (isNaN(edad2)){
    console.log("Esta esta variable no contiene solo numeros")
}
else{
    if (edad2 >= 18){
        console.log("Puede votar")
    }
    else{
        console.log("Es joven para votar")
    }
}


//Operador ternario 

