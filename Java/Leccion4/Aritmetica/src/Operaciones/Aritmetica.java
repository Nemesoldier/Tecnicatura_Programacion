
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //El contructor es un metodo especial
    public Aritmetica(){ //Constructor 1
        System.out.println("Se esta ejecutando el contructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de contructores
    public Aritmetica(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el contructor numero dos");
    }
    

//Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
        
    }
    public int sumarConRetorno(){
       // int resultado = a + b;
        return this.a + this.b;
    }
    public int sumarconArgumentos(int a, int b){
        this.a = a;  //El argumento A se asigna al atributo this.
        this.b = b;
       // return a + b;
       return sumarConRetorno();
    }
}
