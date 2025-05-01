package paquete2;

public class Clase4 {

    private String atributoPrivado = "atributo Privado";

    private Clase4() {
        System.out.println("Constructor privado");
    }
// Creamos un constructor público para poder crear objetos

    public Clase4(String argumento) { // Aquí se puede llamar al constructor vacío
        this();
        System.out.println("Constructor público");
    }

// Método privado
    private void metodoPrivado() {
        System.out.println("Método privado");
    }

    public String getAtributoPrivado() {
        return atributoPrivado;
    }

    public void setAtributoPrivado(String atributoPrivado) {
        this.atributoPrivado = atributoPrivado;
    }
    
    
}
