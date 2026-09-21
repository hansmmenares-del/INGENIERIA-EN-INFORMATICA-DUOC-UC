public class Pez{

    private String nombre;
    private double peso;
    private double longitud;

        // CONSTRUCTOR
    public Pez(
        String nombre,
        double peso,
        double longitud) {
            this.nombre = nombre;
            this.peso = peso;
            this.longitud = longitud;
    }

    public void info(Pez pez) {
        System.out.println(
        "NOMBRE DEL PEZ: "
        +
        pez.getNombre(pez)
        +
        "\n"
        +
        "PESO DEL PEZ (Kg): "
        +
        pez.getPeso(pez)
        +
        "\n"
        +
        "LONGITUD DEL PEZ (metros):"
        +
        pez.getLongitud(pez)
        +
        "\n"
        );
    }
    public void sonido(Pez pez) {
        System.out.println("°oO0°°OGLUP oOo°0 GLUP °°o°0 GLUP!!°°oO");
    }

    // GETTERS Y SETTERS
    public String getNombre(Pez pez) {
        return this.nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPeso(Pez pez) {
        return this.peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    
    public double getLongitud(Pez pez) {
        return this.longitud;
    }
    public void setLongitud(double longitud) {
        this.longitud = longitud;
    }
}