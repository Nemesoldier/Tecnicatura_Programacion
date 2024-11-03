
package matrices;

import java.util.Scanner;


public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Ingresar tamaño de la matriz
        System.out.print("Ingrese el número de filas (n): ");
        int n = sc.nextInt();
        System.out.print("Ingrese el número de columnas (m): ");
        int m = sc.nextInt();
        
        // Crear la matriz de tamaño n x m
        int[][] matriz = new int[n][m];
        
        // Cargar la matriz con valores ingresados por el usuario
        System.out.println("Ingrese los valores para la matriz:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                matriz[i][j] = sc.nextInt();
            }
        }
        
        // Calcular y mostrar la suma de cada fila
        System.out.println("\nSuma de cada fila:");
        for (int i = 0; i < n; i++) {
            int sumaFila = 0;
            for (int j = 0; j < m; j++) {
                sumaFila += matriz[i][j];
            }
            System.out.println("Suma de la fila " + i + ": " + sumaFila);
        }
        
        // Calcular y mostrar la suma de cada columna
        System.out.println("\nSuma de cada columna:");
        for (int j = 0; j < m; j++) {
            int sumaColumna = 0;
            for (int i = 0; i < n; i++) {
                sumaColumna += matriz[i][j];
            }
            System.out.println("Suma de la columna " + j + ": " + sumaColumna);
        }
    }
}
