package peces;

public abstract class Pez {
// ATRIBUTOS
    private String nombre;
    private double peso;
    private double longitud;

// CONSTRUCTOR
    public Pez (
        String nombre,
        double peso,
        double longitud
    )
    throws Exception
    {
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("Invalido! El nombre del pez no puede ser null ni estar vacio.");
        }
        if (peso <= 0) {
            throw new IllegalArgumentException("Invalido! El peso del pez no puede ser inferior a 0.");
        }
        if (longitud <= 0) {
            throw new IllegalArgumentException("Invalido! La longitud del pez no puede ser inferior a 0.");
        } else {
            this.nombre = nombre;
            this.peso = peso;
            this.longitud = longitud;
        }
    }

// FUNCIONES
    public abstract String getTipo();
    public abstract String curiosidad();
    public abstract String sonido();

    public void info() {
        System.out.println(
            "\n"
            +
            "--------"
            +
            "\n"
            +
            getTipo()
            +
            "\n"
            +
            "NOMBRE: " + this.nombre
            +
            "\n"
            +
            "LONGITUD: " + this.longitud
            +
            "\n"
            +
            "PESO: " + this.peso
            +
            "\n");
    }
    
// GETTERS & SETTERS
    public String getNombre(){
        return this.nombre;
    }
    public double getPeso() {
        return this.peso;
    }
    public double getLongitud() {
        return this.longitud;
    }

    public void setNombre(String nombre) throws Exception
    {
        if (nombre == null || nombre.isBlank()) {
            throw new Exception("Invalido! El nombre del pez no puede ser null ni estar vacio.");
        } else {
            this.nombre = nombre;
        }
    }
    public void setPeso(double peso) throws Exception
    {
        if (peso <= 0) {
            throw new IllegalArgumentException("Error: no se puede asignar valor peso inferior o igual a 0.");
        } else {
            this.peso = peso;
        }
    }
    public void setLongitud(double longitud) throws Exception
    {
        if (longitud <= 0) {
            throw new IllegalArgumentException("Error: no se puede asignar valor longitud inferior o igual a 0.");
        } else {
            this.longitud = longitud;
        }
    }    
}
