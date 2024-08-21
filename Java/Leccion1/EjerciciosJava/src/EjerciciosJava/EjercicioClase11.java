
package EjerciciosJava;

import java.util.Scanner;

/**
 *
 * @author USUARIO
 */
public class EjercicioClase11 {
    public static void main(String[] args) {
//        Scanner entrada = new Scanner (System.in);
//        System.out.println("Nota 1: ");
//        var nota1 = Integer.parseInt(entrada.nextLine());
//        System.out.println("Nota 2:");
//        var nota2 = Integer.parseInt(entrada.nextLine());
//        System.out.println("Nota 3:");
//        var nota3 = Integer.parseInt(entrada.nextLine());
//        
//        var  promedio = (nota1 + nota2 + nota3)/3;
//        
//        if (promedio >= 70){
//            System.out.println("El alumno esta aprobado con: " +promedio);
//        }
//        else if (promedio <= 70){
//            System.out.println("El alumno esta desaprobado con: "+promedio);
//        }
//          Scanner entrada = new Scanner (System.in);
//          System.out.println("Monto a pagar: ");
//          var producto = Double.parseDouble(entrada.next());
//          double descuento = 0;
//          
//          if(producto > 100){
//              descuento = producto * 0.2;
//          }
//          double precioFinal = producto - descuento;
//          System.out.println("El precio a pagar es: "+precioFinal);
//            Scanner entrada = new Scanner (System.in);
//            System.out.println("Numero 1: ");
//            var num1 = Integer.parseInt(entrada.nextLine());
//            System.out.println("Numero 2:");
//            var num2 = Integer.parseInt(entrada.nextLine());
//            int resultado;
//            
//            if (num1 == num2){
//                resultado = num1 * num2;
//            }
//            else if (num1 > num2){
//                resultado = num1 - num2;
//            }
//            else{
//                resultado = num1 + num2;
//            }
//            System.out.println("El resultado es: "+resultado);
//              
//            Scanner scanner = new Scanner (System.in);
//            System.out.println("Digite el numero de horas: ");
//            int totalHoras = scanner.nextInt();
//            int semanas = totalHoras /  (7*24);
//            int dias = (totalHoras % (7*24))/24;
//            int horas = totalHoras% 24;
//            System.out.println(totalHoras + " El total de horas es:");
//            System.out.println(semanas + "semanas" + dias + "dias y");
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.println("Ingrese el valor de a: ");
//        double a = scanner.nextDouble();
//        
//        System.out.println("Ingrese el valor de b: ");
//        double b = scanner.nextDouble();
//
//        double cuadradoDeLaSuma = Math.pow((2 * a + 2 * b), 2);
//
//        System.out.println("El cuadrado de la suma de " + a + " y " + b + " es: " + cuadradoDeLaSuma);

            
          Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese la calificación de participación (10%): ");
        double participacion = scanner.nextDouble();

        System.out.println("Ingrese la calificación del primer examen parcial (25%): ");
        double primerParcial = scanner.nextDouble();

        System.out.println("Ingrese la calificación del segundo examen parcial (25%): ");
        double segundoParcial = scanner.nextDouble();

        System.out.println("Ingrese la calificación del examen final (40%): ");
        double examenFinal = scanner.nextDouble();

        double calificacionFinal = (participacion * 0.1) + (primerParcial * 0.25) + (segundoParcial * 0.25) + (examenFinal * 0.4);

        System.out.println("La calificación final del estudiante es: " + calificacionFinal);
              
    
        

        
    }
}

 
    
