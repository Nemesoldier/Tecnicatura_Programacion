//Ejercicio 3: Crear y cargar una matriz de tamaño 3x3 trasponerla y mostrarla
package matrices;

import java.util.Scanner;


public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matriz = new int[3][3];
        int[][] transpuesta = new int[3][3];

        // Cargar la matriz con valores ingresados por el usuario
        System.out.println("Ingrese los valores para una matriz 3x3:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                matriz[i][j] = sc.nextInt();
            }
        }

        // Calcular la matriz transpuesta
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                transpuesta[j][i] = matriz[i][j];
            }
        }

        // Mostrar la matriz original
        System.out.println("\nMatriz Original:");
        mostrarMatriz(matriz);

        // Mostrar la matriz transpuesta
        System.out.println("\nMatriz Transpuesta:");
        mostrarMatriz(transpuesta);
    }

    // Método para mostrar una matriz
    public static void mostrarMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}

