
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /* System.out.println("Hola mundo desde Java");      
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
         */
 /*String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos Creciendo";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en progrmacion";
        System.out.println(miVariable);
         */

 /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
         */
 /*var usuario = "pepe";
        var titulo = "Ingeniero";
        var union = usuario + " " + titulo;
        System.out.println("union = " + union);
         */
 /*var nombre = "Matias";
        var a = 3;
        var b = 2;
        System.out.println(union + " " + (a + b ));
        System.out.println("\t\t\t.:Menu:.");
        System.out.println("\nNueva linea: \n"+nombre);
        System.out.println("Tabulador \t"+nombre);
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");
         */
 /* Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
         */
 /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor miinimo del byte:"+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del byte:"+ Byte.MAX_VALUE);
        
        short numeroShort = 32767;
        System.out.println("numeroShort = " + numeroShort);
        System.out.println("Valor miinimo del short:"+ Short.MIN_VALUE);
        System.out.println("Valor maximo del short:"+ Short.MAX_VALUE);
        
        int numeroEntero = 2147483647;
        System.out.println("numeroEntero = " + numeroEntero);
        System.out.println("Valor miinimo del int:"+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int:"+ Integer.MAX_VALUE);
        
        long numeroLong = 9223372036854775806L;
        System.out.println("numeroLong = " + numeroLong);
        System.out.println("Valor miinimo del long:"+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long:"+ Long.MAX_VALUE);
         */
 /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El numero maximo flotante es:"+ Float.MAX_VALUE);
        System.out.println("El numero minimo flotante es:"+ Float.MIN_VALUE);
        
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El numero double maximo es:"+ Double.MAX_VALUE);
        System.out.println("El numero minimo double es:"+Double.MIN_VALUE);*/
 /* var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        //Tipos primitivos Char
        /*char variableChar = 'a';
        System.out.println("variableChar = " + variableChar);
        
        char varCaracter = '\u0024'; // Indicamos la asignacion con el codigo Unicode
        System.out.println("caracter = " + varCaracter);
        char caracterDecimal = 36;//Valor decimal del juego de caracter
        System.out.println("caracterDecimal = " + caracterDecimal);
        char varcaracterSimbolo = '$'; //Caracter especial podemos copiar y pegar desde Unicode, si no esta en el teclado
        System.out.println("varcaracterSimbolo = " + varcaracterSimbolo);
        
         var varCaracter1 = '\u0024'; // Indicamos la asignacion con el codigo Unicode
        System.out.println("caracter = " + varCaracter1);
        var caracterDecimal1 = (char)36;//Valor entero, le asigna tipo int
        System.out.println("caracterDecimal = " + caracterDecimal1);
        var varcaracterSimbolo1 = '$'; //Caracter especial podemos copiar y pegar desde Unicode, si no esta en el teclado
        System.out.println("varcaracterSimbolo = " + varcaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'g';
        System.out.println("caracterChar = " + caracterChar);
         */
        //Tipos primitivos tipos booleanos
        /*
       var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if (varBool) {
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("La bandera es roja");
        }
        //ALgoritmo ¿Es mayor de edad?
        var edad = 18;
        var edadAdulto = edad >= 18;
        if (edad >= 18){
        System.out.println("Es mayor de edad");
        }
        else{
            System.out.println("Es menor de edad");
        }
         */
        //Conversion de tipos primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " + valorPI);
//        
////        //Pedir un valor
//       var entrada = new Scanner(System.in);
////        System.out.println("Digite su edad: ");
////        edad = Integer.parseInt( entrada.nextLine());
////        System.out.println("edad = " + edad);  
//        
//        //Conversion de tipos primitivos 2
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//        
//        var fraseChar = "Programadores".charAt(12);
//        System.out.println("fraseChar = " + fraseChar);
//        System.out.println("Digite un caracter: ");
//        fraseChar = entrada.nextLine().charAt(1);
//        System.out.println("fraseChar = " + fraseChar);
//
//           int num1 = 5, num2 = 4;
//           var solucion = num1 + num2;
//           System.out.println("Solucion de la suma = " + solucion);
//           
//           solucion = num1 - num2;
//           System.out.println("Solucion de la resta = " + solucion);
//           
//           solucion = num1 * num2;
//           System.out.println("Solucion de la multiplicacion es = " + solucion);
//           
//           solucion = num1 / num2;
//           System.out.println("Solucion de la division es = " + solucion);
//        
//           var solucion2 = 3.4 / num2;
//           System.out.println("la solucion 2 es = " + solucion2);
//        
//           solucion = num1 % num2;
//           System.out.println("solucion = " + solucion);
//           
//           if (num2 % 2 == 0)
//               System.out.println("Es un numero par");
//           else
//               System.out.println("Es un numero impar");

        /* int varNum1 = 1, varNum2 = 4;
            int varNum3 = varNum1 + 6 - varNum2;
            System.out.println("varNum3 = " + varNum3);
           
            varNum1 += 1;
            System.out.println("varNum1 = " + varNum1);
            
            varNum1 -= 1;
            System.out.println("varNum1 = " + varNum1);
            
            varNum1 *= 1;
            System.out.println("varNum1 = " + varNum1);*/
        //Operadores unarios: cambio de signo
        /* var varA = 7;
           var varB = -varA;
           System.out.println("varA = " + varA);
           System.out.println("varB = " + varB); //El resultado sera un numero negativo
           
           //Operador de negacion
           var varC = true; //Esta literal por default en java es de tipo boolean
           var varD = !varC; // Aqui esta invirtiendo el valor
           System.out.println("varC = " + varC);
           System.out.println("varD = " + varD);
           
           //Operadores unarios de incremento: Preincremento
           var varE = 9; //se va a modificar su valor
           var varF = ++ varE; //Simbolo antes de la variable
           System.out.println("varE = " + varE); //Se incrementa en la unidad
           System.out.println("varF = " + varF); //Se va a sumar 1
           
            //Post incremento, el simnolo va despues de la variable
            var varG = 3;
            var varH = varG++; //Primero va el valor de la variable despues el incremento
            System.out.println("varG = " + varG);
            System.out.println("varH = " + varH);
            
            //Operadores unarios de decremento: Pre-decremento
            var varI = 4;
            var varJ = --varI;
            System.out.println("varI = " + varI); //La variable ya esta con decremento
            System.out.println("varJ = " + varJ);
            
            //Postdecremento
            var varK = 8;
            var varL = varK--; //Primero el valor de la variable, luego viene el decremento
            System.out.println("vark = " + varK);//Aqui va a decrementar en L
            System.out.println("varL = " + varL); */
        //Operadores de igualdad y relacionales
        /* var numA = 5;
        var numB = 4;
        var numC = (numA == numB);
        System.out.println("numC = " + numC);

        var numD = numA != numB;
        System.out.println("numD = " + numD);

        var cadenaA = "Hola";
        var cadenaB = "Hola";
        var cadenaC = cadenaA == cadenaB;
        System.out.println("cadenaC = " + cadenaC);

        var varD = cadenaA.equals(numB);
        System.out.println("cadenaC = " + cadenaC);

        var Gvar = numA > numB;
        System.out.println("Gvar = " + Gvar);

        if (numA % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("el numero es impar");
        }

        var edad = 17;
        var edadAdulto = 18;
        if (edad >= edadAdulto){
            System.out.println("Usted es mayor de edad");
        }
        else
            System.out.println("Usted es menor de edad");*/
        //Operador condicional And 
        /* var valorA = 20;
       var valorMax = 10;
       var valorMin = 0;
       var respuesta = valorA >= 0 && valorA <= 10;
       
       if (respuesta){
           System.out.println("El valor esta dentro del rango");
       }
       else{
           System.out.println("El valor esta fuera del rango");
       }
        //Operador condicional Or   
       var vacaciones = false;
       var diaLibre = true;
       if (vacaciones || diaLibre){
           System.out.println("Tiene el dia libre");
       }
       else{
           System.out.println("Anda a labura bobo");
       }*/
        //OPErador ternario
        /*var resultadoT = (5 > 6) ? "Verdadero" : "Falso";
    System.out.println("resultadoT = " + resultadoT);
    
    var numeroT = 6;
    resultadoT = (numeroT % 2 == 0) ? "Es par":"Es impar";
        System.out.println("resultadoT = " + resultadoT);
         */
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x); //6
        System.out.println("y = " + y); //9
        System.out.println("z = " + z); //16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica); // 4 + ((5 * 6) / 3 = 30 / 3 = 10 + 4 = 14
        
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica); //4 + 5 = 9 * 6 = 54 / 3 = 18

        
    
    
    }

}
