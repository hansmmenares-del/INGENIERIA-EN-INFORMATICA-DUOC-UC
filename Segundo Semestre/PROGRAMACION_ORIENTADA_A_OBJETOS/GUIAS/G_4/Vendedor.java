public class Vendedor extends Empleado {
    
    double comisionPorVenta;
    int numeroDeVentas;

    Vendedor(String nombre, double sueldoBase, double comisionPorVenta, int numeroDeVentas) {

        super(nombre, sueldoBase);
        this.comisionPorVenta = comisionPorVenta;
        this.numeroDeVentas = numeroDeVentas;

    }

    @Override
    public double calcularSuledo() {

        return this.sueldoBase + (this.comisionPorVenta * this.numeroDeVentas);

    }
}