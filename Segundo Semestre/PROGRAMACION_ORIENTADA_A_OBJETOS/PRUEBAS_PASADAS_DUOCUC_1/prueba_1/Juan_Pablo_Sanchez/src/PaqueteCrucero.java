public class PaqueteCrucero extends PaqueteTuristico{
    private Boolean conBalcon;

    public PaqueteCrucero(String destino, int duracion, Pasajero pasajero, Boolean conBalcon) {
        super(destino, duracion, pasajero);
        this.conBalcon = conBalcon;
    }
    @Override
    public double calcularCosto(){
        return conBalcon ? 800000 * 1.25 : 800000;
    }
    @Override
    public String getTipo(){
        return conBalcon ? "Paquete crucero con balcon" : "Paquete sin balcon";
    }
}
