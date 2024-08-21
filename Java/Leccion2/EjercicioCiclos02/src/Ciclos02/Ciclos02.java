/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ciclos02;

import javax.swing.JOptionPane;
public class Ciclos02 {public static void main(String[] args) {
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

