public class Main{
    public static void main(String [] args){
        // (5) Crear Objetos distintos:
        Producto cosa_a = new Producto("cosa_a", 199.99, 100, "KA3020");
        Producto cosa_b = new Producto("cosa_b", 300.85, 120, "KA3021");
        Producto cosa_c = new Producto("cosa_c", 97.30, 130, "KA3022");

        // (6) Mostrar info usando metodo mostrarInformaciom(), aplicar descuento, calcular valor inventario, verificar stock con hayStock().
        System.out.println(
            "\n_______________\n"
            +
            "\n--Primera fase--\n");
            cosa_a.mostrarInformacion();
            cosa_b.mostrarInformacion();
            cosa_c.mostrarInformacion();
        System.out.println(
            "\n_______________\n"
            +
            "\n--Segunda fase--\n");
            cosa_a.aplicarDescuento(15);
            cosa_a.mostrarInformacion();
            cosa_b.aplicarDescuento(0);
            cosa_b.mostrarInformacion();
            cosa_c.aplicarDescuento(0);
            cosa_c.mostrarInformacion();

        System.out.println(
            "\n_______________\n"
            +
            "\n--Tercera fase--\n"
        );
        cosa_a.mostrarInformacion();
        cosa_a.calcularValorTotal(cosa_a.getPrecio(), cosa_a.getCantidadEnStock());
        cosa_b.mostrarInformacion();
        cosa_b.calcularValorTotal(cosa_b.getPrecio(), cosa_b.getCantidadEnStock());
        cosa_c.mostrarInformacion();
        cosa_c.calcularValorTotal(cosa_c.getPrecio(), cosa_c.getCantidadEnStock());
        
        System.out.println(
            "\n_______________\n"
            +
            "\n--Tercera fase--\n"
        );
        cosa_a.mostrarInformacion();
        cosa_a.hayStock();
        cosa_a.mostrarInformacion();
        cosa_b.hayStock();
        cosa_a.mostrarInformacion();
        cosa_c.hayStock();

    }
}
// (1) Crear clase, en este caso "Producto". Fuera de la clase publica Main{}
class Producto{
    // (2) Definir atributos de la clase
    String nombre;
    double precio;
    int cantidadEnStock;
    String codigo;

    // (3) Crear Constructor de la clase, en este caso "Producto"
    // CONSTRUCTOR //
    Producto(String nombre, double precio, int cantidadEnStock, String codigo){
        // Al momento de instanciar se necesitan todos los argumentos, o sea, al crear un producto nuevo, se necesitan estos datos.
        this.nombre = nombre;
        this.precio = precio;
        this.cantidadEnStock = cantidadEnStock;
        this.codigo = codigo;
    }
    // (4) Metodos de la clase
    double calcularValorTotal(double precio, int cantidadEnStock){
        double valorTotalDelStock = precio * cantidadEnStock;
        System.out.println(
            "VALOR TOTAL DEL INVENTARIO: " + "$" + valorTotalDelStock
            +
            "\n[Calculo - ($"
            +
            this.precio
            +
            " * "
            +
            this.cantidadEnStock
            +
            " Unidades)]"
    );
        return valorTotalDelStock;
    }
    double aplicarDescuento(double porcentaje){
        if (porcentaje >= 0) {
            precio -= precio * porcentaje/100;
            return precio;
        }
        else {
            System.out.println("Error: value 'descuento' must be positive");
            return precio;
        }
    }

    void mostrarInformacion(){
        System.out.println(
            "________________" + "\n" +
            "CODIGO PRODUCTO: " +
            Producto.this.codigo + "\n" +
            "NOMBRE PRODUCTO: " +
            Producto.this.nombre + "\n" +
            "PRECIO PRODUCTO: " +
            Producto.this.precio + "\n" +
            "CANTIDAD EN STOCK: " +
            Producto.this.cantidadEnStock + " Unidades"
        );
    }

    boolean hayStock(){
        if (cantidadEnStock > 0) {
            System.out.println("\nSI HAY STOCK :D\n\n");
            return true;
        }
        else {
            System.out.println("\nNO HAY STOCK D:\n\n");
            return false;
        }
    }

    double getPrecio(){
        return this.precio;
    }
    int getCantidadEnStock(){
        return this.cantidadEnStock;
    }
}