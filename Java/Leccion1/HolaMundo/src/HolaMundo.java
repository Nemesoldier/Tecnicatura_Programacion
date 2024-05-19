
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
       // var edadAdulto = edad >= 18;
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
//        //Pedir un valor
       var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt( entrada.nextLine());
//        System.out.println("edad = " + edad);  
        
        //Conversion de tipos primitivos 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "Programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(1);
        System.out.println("fraseChar = " + fraseChar);
        
        
                
        
        
    }
    
}
