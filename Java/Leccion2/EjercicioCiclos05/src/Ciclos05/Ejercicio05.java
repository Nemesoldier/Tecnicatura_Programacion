package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random() * 100); // Esto genera un número aleatorio
        
        do {
            String entrada = JOptionPane.showInputDialog("Digite un número:");
            numero = Integer.parseInt(entrada);
            
            if (numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un número mayor");
            } else if (numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un número menor");
            } else {
                JOptionPane.showMessageDialog(null, "¡Felicidades! Has adivinado el número.");
            }
            conteo++;
        } while (numero != aleatorio);
        
        JOptionPane.showMessageDialog(null, "Adivinaste el número en " + conteo + " intentos.");
    }
}

