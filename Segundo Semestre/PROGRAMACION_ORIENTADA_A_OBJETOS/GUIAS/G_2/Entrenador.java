public class Entrenador{

    String nombre;
    String especialidad;
    int aniosExperiencia;

    Entrenador(String nombre, String especialidad, int aniosExperiencia){
        this.nombre = nombre;
        this.especialidad = especialidad;
        this.aniosExperiencia = aniosExperiencia;
    }

    void mostrarInformacion(){
        System.out.println(
            "______________________"
            +
            "\n"
            +
            "NOMBRE DE ENTRENADOR: "
            +
            Entrenador.this.nombre
            +
            "\n"
            +
            "ESPECIALIDAD: "
            +
            Entrenador.this.especialidad
            +
            "\n"
            +
            "AÑOS DE EXPERIENCIA: "
            +
            Entrenador.this.aniosExperiencia
        );
    }
    boolean esExperto(){
        if (Entrenador.this.aniosExperiencia >= 5){
            System.out.println("________\nE");
            return true;
        }
        else {
            return false;
        }
    }
    String getNombreEntrenador(){
        return this.nombre;
    }
    String getEspecialidad(){
        return this.especialidad;
    }
}