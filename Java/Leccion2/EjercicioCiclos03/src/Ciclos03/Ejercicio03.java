package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        String entrada = JOptionPane.showInputDialog("Digite un número: ");
        numero = Integer.parseInt(entrada);
        
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es PAR");
            } else {
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es IMPAR");
            }
            entrada = JOptionPane.showInputDialog("Digite otro número: ");
            numero = Integer.parseInt(entrada);
        }
        
        JOptionPane.showMessageDialog(null, "El número ingresado es " + numero + ". Finaliza el programa.");
    }
}
