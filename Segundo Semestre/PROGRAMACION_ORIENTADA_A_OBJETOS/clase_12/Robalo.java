public class Robalo extends Pez {
    double profundidadHabitat;
    public Robalo(
            String nombre,
            double peso,
            double longitud,
            double profundidadHabitat) {
        super(
                nombre,
                peso,
                longitud);
        this.profundidadHabitat = profundidadHabitat;
    }
}