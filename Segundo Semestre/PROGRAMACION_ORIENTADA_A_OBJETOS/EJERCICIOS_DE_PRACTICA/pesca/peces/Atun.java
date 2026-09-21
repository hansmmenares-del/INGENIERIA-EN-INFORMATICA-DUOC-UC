package peces;

public class Atun extends Pez {
// ATRIBUTOS
    String nombre;
    double peso;
    double longitud;
    double velocidadNado;
    
// CONSTRUCTOR
    public Atun(
        String nombre,
        double peso,
        double longitud,
        double velocidadNado
    ) throws Exception {
        super(nombre, peso, longitud);
        if (velocidadNado <= 0) {
            throw new IllegalArgumentException("Invalido! Velocidad de nado del pez debe ser mayor que 0.");
        } else {
            this.velocidadNado = velocidadNado;
        }
    }

// FUNCIONES
    @Override
    public String getTipo() {
        return "ATUN";
    }
    @Override
    public String sonido() {
        return "GLUP! glorbUrl sLOp!!";
    }
    @Override
    public String curiosidad() {
        return this.nombre + "..." + "\nLa velocidad de nado de este " + getTipo() + " es de: " + this.velocidadNado + " KM/H" + "\n" + sonido();
    }
// GETTERS & SETTERS (ATRIBUTOS ESPECIALES)
    public double getVelocidadNado() {
        return this.velocidadNado;
    }

    public void setVelocidadNado(double velocidadNado) throws Exception {
        if (velocidadNado <= 0) {
            throw new IllegalArgumentException("Invalido! La velocidad de nado del pez debe ser mayor que 0.");
        } else {
            this.velocidadNado = velocidadNado;
        }
    }
}