package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;

        String entrada = JOptionPane.showInputDialog("Digite un número: ");
        numero = Integer.parseInt(entrada);

        while (numero >= 0) {
            JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            conteo++;
            entrada = JOptionPane.showInputDialog("Digite otro número: ");
            numero = Integer.parseInt(entrada);
        }

        JOptionPane.showMessageDialog(null, "Ha ingresado " + conteo + " números que no son negativos.");
    }
}

