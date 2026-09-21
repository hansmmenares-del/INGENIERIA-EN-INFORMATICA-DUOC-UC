public abstract class PaqueteTuristico {

int duracionEnDias;
int costoTotal;
int costoSinImpuesto;

    public PaqueteTuristico(
        Pasajero pasajero,
        int duracionEnDias,
        int costoTotal,
        int costoSinImpuesto)
        {
            this.pasajero = pasajero;
            this.duracionEnDias = duracionEnDias;
            this.costoTotal = costoTotal;
            this.costoSinImpuesto = costoSinImpuesto;
        }
}