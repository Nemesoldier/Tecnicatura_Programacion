
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
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
