
package test;

public class TestArreglos {
    public static void main(String[] args) { //Lado derecho instanciamos un objeto de tipo object
        int edades[] = new int [3];  //El ladoi izquierdo declaramos la variable
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        edades[1] = 22;
        System.out.println("edades 2 = " + edades[2]);
        
        edades[2] = 18;
                System.out.println("edades 2 = " + edades[2]);
         
        //edades [3] = 7; //Fuera de rango, error en la ejecucion
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos"+1+": "+edades[i]);
        }
    }
}
