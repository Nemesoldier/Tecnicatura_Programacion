package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        // Crear productos
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Zapatos", 12000.00);
        Producto producto4 = new Producto("Camisa", 7500.00);
        Producto producto5 = new Producto("Bufanda", 2500.00);
        Producto producto6 = new Producto("Cinturon", 3200.00);
        Producto producto7 = new Producto("Gorro", 1800.00);
        Producto producto8 = new Producto("Guantes", 2200.00);
        Producto producto9 = new Producto("Saco", 15900.00);
        Producto producto10 = new Producto("Corbata", 1500.00);

        // Crear la primera orden y agregar productos
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.mostrarOrden();

        // Crear la segunda orden y agregar productos
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();
    }
}

