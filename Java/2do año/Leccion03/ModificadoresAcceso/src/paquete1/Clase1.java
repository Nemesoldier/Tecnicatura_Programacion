
package paquete1;

public class Clase1 {
    public String atributoPublico = "Valor atributo public";
    protected String atributoProtected = "valor atributo protected";

    public Clase1() {
        System.out.println("Constructor public");
    }

    protected Clase1(String atributoPublico) {
        System.out.println("Constructor protected");
    }

    public void metodoPublico() {
        System.out.println("Método publico");
    }
}
