package peces;

public class Robalo extends Pez {
// ATRIBUTOS
    String nombre;
    double peso;
    double longitud;
    double profundidadHabitat;
    
// CONSTRUCTOR
    public Robalo(
        String nombre,
        double peso,
        double longitud,
        double profundidadHabitat
    ) throws Exception {
        super(nombre, peso, longitud);
        if (profundidadHabitat <= 0) {
            throw new IllegalArgumentException("Invalido! La profundidad de habitat del pez debe tener un valor mayor que 0.");
        } else {
            this.profundidadHabitat = profundidadHabitat;
        }
    }

// FUNCIONES
    @Override
    public String getTipo() {
        return "ROBALO";
    }
    @Override
    public String sonido() {
        return "GLUPEERS!!-glupitilup...GLAP!";
    }
    @Override
    public String curiosidad() {
        return getNombre() + "..." + "\nEste " + getTipo() + " se encuentra a una profundidad de: " + getProfundidadHabitat() + "\n" + sonido();
    }

// GETTERS & SETTERS (ATRIBUTOS ESPECIALES)
    public double getProfundidadHabitat() {
        return this.profundidadHabitat;
    }
    public void setProfundidadHabitat(double profundidadHabitat) throws Exception {
        if (profundidadHabitat <= 0) {
            throw new IllegalArgumentException("Invalido! La profundidad de habitat del pez debe tener un valor mayor que 0.");
        } else {
            this.profundidadHabitat = profundidadHabitat;
        }
    }
}