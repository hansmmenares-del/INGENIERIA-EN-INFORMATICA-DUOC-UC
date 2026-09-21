public class Salmon extends Pez {
    String origenRio;
    public Salmon(
            String nombre,
            double peso,
            double longitud,
            String origenRio){
        super(
                nombre,
                peso,
                longitud);
        this.origenRio = origenRio;
    }
}