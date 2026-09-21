public class PaqueteInternacional extends PaqueteTuristico implements Asegurable {
    private Boolean primeraClase;
    private String seguro;

    // Se agrega 'Boolean primeraClase' en los parámetros del constructor
    public PaqueteInternacional(String destino, int duracion, Pasajero pasajero, Boolean primeraClase) {
        super(destino, duracion, pasajero);
        this.primeraClase = primeraClase;
    }

    @Override
    public double calcularCosto() {
        return primeraClase ? 450000 * 1.35 : 450000;
    }

    @Override
    public String getTipo() {
        return "Paquete Internacional";
    }

    @Override
    public String contratarSeguro(String compania) {
        if (compania.isBlank()) {
            throw new IllegalArgumentException("Debe seleccionar una compañía.");
        }
        if (this.seguro != null) {
            throw new IllegalArgumentException("El paquete ya cuenta con un seguro.");
        }
        this.seguro = compania;
        return "Seguro contratado con la compañía " + compania;
    }

    @Override
    public String consultarSeguro() {
        return (this.seguro == null) ? "Sin seguro contratado" : "Seguro contratado por " + this.seguro;
    }
}