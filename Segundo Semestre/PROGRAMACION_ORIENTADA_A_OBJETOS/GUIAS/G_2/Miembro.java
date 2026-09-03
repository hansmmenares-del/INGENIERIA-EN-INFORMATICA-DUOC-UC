public class Miembro{
    
    String nombre;
    int edad;
    boolean mensualidadPagada = false;
    String entrenadorAsignado;
    String especialidad;

    Miembro(String nombre, int edad, boolean mensualidadPagada, Entrenador entrenadorAsignado) {
        this.nombre = nombre;
        this.edad = edad;
        this.mensualidadPagada = mensualidadPagada;
        this.entrenadorAsignado = entrenadorAsignado.getNombreEntrenador();
        this.especialidad = entrenadorAsignado.getEspecialidad();
    }

    void pagarMensualiad(){
        this.mensualidadPagada = true;
        System.out.println("__________\nPAGO CONFIRMADO! :D\n__________");
    }

    void mostrarInformacion(){
        System.out.println(
            "NOMBRE DE MIEMBRO: "
            +
            this.nombre
            +
            "\n"
            +
            "EDAD: "
            +
            this.edad
            +
            " años"
            +
            "\n"
            +
            "ESTADO DE PAGO MENSUALIDAD: "
            +
            this.mensualidadPagada
            +
            "\n"
            +
            "ENTRENADOR ASIGNADO: "
            +
            this.entrenadorAsignado
            +
            "\n"
            +
            "ESPECIALIDAD ENTRENADOR: "
            +
            this.especialidad
        );
    }
    boolean puedeEntrenar(){
        if (this.mensualidadPagada == true) {
            return true;
        }
        else {
            return false;
        }
    }
}