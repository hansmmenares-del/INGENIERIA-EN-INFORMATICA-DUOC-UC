package peces;

public class Salmon extends Pez {
// ATRIBUTOS
    String nombre;
    double peso;
    double longitud;
    String origenRio;
    
// CONSTRUCTOR
    public Salmon(
        String nombre,
        double peso,
        double longitud,
        String origenRio
    ) throws Exception {
        super(nombre, peso, longitud);
        if (origenRio == null || origenRio.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'rio de origen' no puede ser null ni estar vacio.");
        } else {
            this.origenRio = origenRio;
        }
    }

// FUNCIONES
    @Override
    public String getTipo() {
        return "SALMON";
    }
    @Override
    public String sonido() {
        return "GLUP! GLIP GLOP-GLAAAP... sLOpers!!";
    }
    @Override
    public String curiosidad() {
        return this.nombre + "..." + "\nEl rio de origen de este " + getTipo() + " es de: " + this.origenRio + "\n" + sonido();
    }

// GETTERS & SETTERS (ATRIBUTOS ESPECIALES)
    public String getOrigenRio() {
        return this.origenRio;
    }
    public void setOrigenRio(String origenRio) throws Exception {
        if (origenRio == null || origenRio.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'rio de origen' no puede ser null ni estar vacio.");
        } else {
            this.origenRio = origenRio;
        }
    }
}