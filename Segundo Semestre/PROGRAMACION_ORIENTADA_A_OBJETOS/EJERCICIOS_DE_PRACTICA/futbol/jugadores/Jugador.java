package jugadores;

public abstract class Jugador {
    private String nombre;
    private double probabilidadGol;

    public Jugador(
        String nombre,
        double probabilidadGol
    ) throws Exception {
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("Error: nombre esta vacio.");
        }
        if (probabilidadGol <= 0) {
            throw new IllegalArgumentException("Error: probabilidad de gol es menor o igual que 0.");
        }
        this.nombre = nombre;
        this.probabilidadGol = probabilidadGol;
    }
    
    public void patear(Jugador jugadorPateador) throws Exception {
        if (jugadorPateador == null) {
            throw new NullPointerException("Error: Jugador no existe.");
        }
        else if (this.probabilidadGol <= 0) {
            throw new ArithmeticException("Error: Jugador con probabilidad de gol inferior o igual a 0.");
        }
        else if (this.probabilidadGol >= 50) {
            System.out.println("\n\nGOOOL! " + this.nombre + " ha metido el gol! y celebra!!...\n\n");
        } else {
            System.out.println("\n\n" + this.nombre + " ha fallado...\n\n");
        }
    }

    public String getNombre() {
        return this.nombre;
    }
    public double getProbabilidadGol() {
        return this.probabilidadGol;
    }

    public void setNombre(String nombre) throws Exception {
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("Error: nombre esta vacio.");
        } else {
            this.nombre = nombre;
        }
    }
    public void setProbabilidadGol(double probabilidadGol) throws Exception {
        if (probabilidadGol <= 0) {
            throw new IllegalArgumentException("Error: probabilidad de gol es menor o igual que 0.");
        } else {
            this.probabilidadGol = probabilidadGol;
        }
    }
}