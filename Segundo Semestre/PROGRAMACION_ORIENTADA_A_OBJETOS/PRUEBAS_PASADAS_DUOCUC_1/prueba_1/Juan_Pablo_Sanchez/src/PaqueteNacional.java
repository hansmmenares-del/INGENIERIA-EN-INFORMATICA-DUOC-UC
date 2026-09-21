public class PaqueteNacional extends PaqueteTuristico{
    public PaqueteNacional(String destino, int duracion, Pasajero pasajero) {
        super(destino, duracion, pasajero);
    }
    @Override
    public double calcularCosto(){
        return 150000;
    }
    @Override
    public String getTipo(){
        return "Paquete Nacional";
    }

}
