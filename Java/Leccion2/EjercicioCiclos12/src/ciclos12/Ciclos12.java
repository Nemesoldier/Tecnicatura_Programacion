/*
Ejercicio12: Pedir un numero y calcular su factorial, hacerlo con las dos clases
Scanner y JOptionPane
*/
import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Introduce un número: ");
        int numero = scanner.nextInt();
        int factorial = 1;
        
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        
        System.out.println("El factorial de " + numero + " es: " + factorial);
        scanner.close();
    }
}

import javax.swing.JOptionPane;

public class Ciclos12 {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Introduce un número:");
        int numero = Integer.parseInt(input);
        int factorial = 1;
        
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        
        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }
}
