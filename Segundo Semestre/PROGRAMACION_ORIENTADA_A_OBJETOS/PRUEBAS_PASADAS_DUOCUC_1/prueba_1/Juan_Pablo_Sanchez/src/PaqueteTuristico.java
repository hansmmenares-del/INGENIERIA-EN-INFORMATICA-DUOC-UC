public abstract class PaqueteTuristico {
    
// ATRIBUTOS
    private String destino;
    private int duracionEnDias;
    private Pasajero pasajero;
    private double costoFijo;

// CONSTRUCTOR
    public PaqueteTuristico(
        String destino,
        int duracionEnDias,
        Pasajero pasajero,
        double costoFijo) {
            this.destino = destino;
            this.duracionEnDias = duracionEnDias;
            this.costoFijo = costoFijo;
            this.pasajero = pasajero;
        }

    public abstract double calcularPrecioFinal();
    public abstract String getTipo();

    //public double calcularPrecioFinal(double impuesto){
    //    if(impuesto < 0 || impuesto > 100){
    //        throw new IllegalArgumentException("El impuesto debe ser entre 0 y 100");
    //    }
    //    double costoBase = calcularCosto();
    //    return costoBase + (costoBase * (impuesto / 100.0));
    //
    //}

    public String getDestino(PaqueteTuristico paqueteTuristico) {
        return this.destino;
    }
    public int getDuracionEnDias(PaqueteTuristico paqueteTuristico) {
        return this.duracionEnDias;
    }
    public double getCostoFijo(PaqueteTuristico paqueteTuristico) {
        return this.costoFijo;
    }
    public Pasajero getPasajero(PaqueteTuristico paqueteTuristico) {
        return this.pasajero;
    }
    public String getNombreCompletoPasajero(PaqueteTuristico paqueteTuristico) {
        return this.pasajero.getNombreCompleto();
    }
}
