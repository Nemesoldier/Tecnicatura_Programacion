package test;

import static aritmetica.Aritmetica.division;
import excepciones.OperacionExcepcion;
public class TestExcepciones {
    public static void main(String[] args) {
        int resultado = 0;
        try {
            resultado = division(10, 0);
        } catch (OperacionExcepcion e) {
            System.out.println("Ocurrió un error de tipo OperacionExcepcion");
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println("Ocurrió un Error");
            e.printStackTrace(System.out); //se conoce como la pila de excepciones
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Se revisó la división entre cero");
        }
        System.out.println("La variable de resultado tiene como valor: " + resultado);
    }
}