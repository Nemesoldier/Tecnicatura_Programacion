//Ejercicio 2: Leer u numero e indicar si es positivo o negativo
//El proceso se repite hasta qye se introduzaca un 0
//Hacer este ejercicio con la clase Scanner,
//Luego hacerlo con la clase JOptionPane
package Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if(numero > 0){
                System.out.println("El numero "+numero+" es POSITIVO");
                
            }
            else{
                System.out.println("El numero "+numero+" es NEGATIVO");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
//Con la clase JOptionPane
/*package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Digite un número:");
        int numero = Integer.parseInt(entrada);

        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            } else {
                JOptionPane.showMessageDialog(null, "El número " + numero + " es NEGATIVO");
            }

            entrada = JOptionPane.showInputDialog("Digite otro número:");
            numero = Integer.parseInt(entrada);
        }

        JOptionPane.showMessageDialog(null, "El número " + numero + " finaliza el programa");
    }
}
*/


