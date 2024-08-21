//Ejercicio 1 Carcular estacion del año
//Ejercicio 2 Hora del dia

 let  mes = 2;
let  estacion;
if (mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor pertenece al la estacion "+estacion);

/*
let horaDia = 22;
let mensaje;
if (horaDia >= 6 && horaDia <= 11){
    mensaje = "Buenos dias";
}
else if (horaDia >= 12 && horaDia <= 16){
    mensaje = ("Good afternoon");
}
else if (horaDia >= 17 && horaDia <= 19){
    mensaje = ("Good evening");
}
else if (horaDia >= 20 && horaDia <= 23){
    mensaje = ("Good Night");
}
else{
    mensaje = ("Valor incorrecto")
}
console.log(mensaje);
*/
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Verano";
        break;
    default:
        estacion = "Valor incorrecto"
}
console.log("Bienvenido a la estacion de:"+estacion)