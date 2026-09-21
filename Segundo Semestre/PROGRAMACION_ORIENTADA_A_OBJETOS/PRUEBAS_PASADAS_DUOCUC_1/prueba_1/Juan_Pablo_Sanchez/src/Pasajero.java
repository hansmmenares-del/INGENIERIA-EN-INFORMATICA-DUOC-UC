public class Pasajero {
    private String nombre;
    private String pasaporte;
    private String correo;

    public Pasajero(String nombre, String pasaporte, String correo) {

        if(nombre.isBlank() || pasaporte.isBlank() ||correo.isBlank()){
            throw new IllegalArgumentException("Datos invalidos.");
        }
        this.nombre = nombre;
        this.pasaporte = pasaporte;
        this.correo = correo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getPasaporte() {
        return pasaporte;
    }

    public String getCorreo() {
        return correo;
    }
}
