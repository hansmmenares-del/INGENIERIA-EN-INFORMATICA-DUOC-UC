// Empleado (clase base)
// Gerente y Vendedor (subclases)
// Empresa (clase que administra a todos).
public class Main {
    public static void main(String[] args) {

        Empleado empleado_1 = new Empleado("Hans", 5);

        System.out.println("Prueba de programa :D");

        empleado_1.calcularSueldo();

    }
}