
package matrices;


public class Ejercicio4 {
    public static void main(String[] args) {
        int[][] matriz = new int[7][7];

        // Rellenar la matriz
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if (i == j) {
                    matriz[i][j] = 1; // Asignar 1 en la diagonal principal
                } else {
                    matriz[i][j] = 0; // Asignar 0 en el resto
                }
            }
        }

        // Imprimir la matriz
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
