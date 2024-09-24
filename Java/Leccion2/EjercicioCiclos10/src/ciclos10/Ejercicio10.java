package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int numero, suma = 0;
        
        for (int i = 1; i <= 10; i++) {
            // Usamos JOptionPane para pedir un número
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        }
        
        // Mostramos el resultado usando JOptionPane
        JOptionPane.showMessageDialog(null, "La suma de todos los números es: " + suma);
    }
}

