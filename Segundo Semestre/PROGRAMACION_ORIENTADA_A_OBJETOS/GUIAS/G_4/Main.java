public class Main {
    public static void main(String[] args) {

        Empleado empleado_1 = new Empleado("Hans", 5);
        Gerente gerente_1 = new Gerente("Pedro", 10, 3);
        Vendedor vendedor_1 = new Vendedor("Juan", 6, 3, 2);
        Vendedor vendedor_2 = new Vendedor("Diego", 7, 6, 5);
        Empresa empresa_1 = new Empresa("La Gran Empresa", gerente_1, vendedor_1, vendedor_2);


        List<Empleado<Empresa>>
        empresa_1.mostratNomina();
        empresa_1.calcularNominaTotal();

        System.out.println("Prueba de programa :D");

        empleado_1.calcularSueldo();

    }
}