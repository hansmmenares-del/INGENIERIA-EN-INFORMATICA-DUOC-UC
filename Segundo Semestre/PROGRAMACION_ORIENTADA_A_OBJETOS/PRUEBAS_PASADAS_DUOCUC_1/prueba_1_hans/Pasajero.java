public class Pasajero {

// ATRIBUTOS
    String primerNombre;
    String segundoNombre;
    String apellidoPaterno;
    String apellidoMaterno;
    String rut;
    String fechaDeNacimiento;
    String correo;
    int numVisa;
    int pasaporte;

// CONSTRUCTOR
    public Pasajero(
        String primerNombre,
        String segundoNombre,
        String apellidoPaterno,
        String apellidoMaterno,
        String rut,
        String fechaDeNacimiento,
        String correo,
        int numVisa,
        int pasaporte)
        {
            this.primerNombre = primerNombre;
            this.segundoNombre = segundoNombre;
            this.apellidoPaterno = apellidoPaterno;
            this.apellidoMaterno = apellidoMaterno;
            this.rut = rut;
            this.fechaDeNacimiento = fechaDeNacimiento;
            this.correo = correo;
            this.numVisa = numVisa;
            this.pasaporte = pasaporte;
        }

// GETTERS & SETTERS
    public String getNombreCompleto() {
        return this.primerNombre + " " + this.segundoNombre + " " + this.apellidoPaterno + " " + this.apellidoMaterno;
    }
    public String getRut() {
        return this.rut;
    }
    public int getNumVisa() {
        return this.numVisa;
    }
    public String getCorreo() {
        return this.correo;
    }
    public int getPasaporte() {
        return this.pasaporte;
    }
    public String getPrimerNombre() {
        return this.primerNombre;
    }
    public String getSegundoNombre() {
        return this.segundoNombre;
    }
    public String getApellidoPaterno() {
        return this.apellidoPaterno;
    }
    public String getApellidoMaterno() {
        return this.apellidoMaterno;
    }
    public String getFechaDeNacimiento() {
        return this.fechaDeNacimiento;
    }

    public void getRut(String rut) {
        this.rut = rut;
    }
    public void getNumVisa(int numVisa) {
        this.numVisa = numVisa;
    }
    public void getCorreo(String correo) {
        this.correo = correo;
    }
    public void getPasaporte(int pasaporte) {
        this.pasaporte = pasaporte;
    }
    public void getPrimerNombre(String primerNombre) {
        this.primerNombre = primerNombre;
    }
    public void getSegundoNombre(String segundoNombre) {
        this.segundoNombre = segundoNombre;
    }
    public void getApellidoPaterno(String apellidoPaterno) {
        this.apellidoPaterno = apellidoPaterno;
    }
    public void getApellidoMaterno(String apellidoMaterno) {
        this.apellidoMaterno = apellidoMaterno;
    }
    public void getFechaDeNacimiento(String fechaDeNacimiento) {
        this.fechaDeNacimiento = fechaDeNacimiento;
    }
}