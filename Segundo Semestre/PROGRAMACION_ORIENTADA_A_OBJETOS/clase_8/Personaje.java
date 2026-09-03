public class Personaje {

    String nombre;
    double ataque;
    double vida;
    String estado;

    Personaje(String nombre, double ataque, double vida, String estado) {

        this.nombre = nombre;
        this.ataque = ataque;
        this.vida = vida;
        this.estado = estado;

    }

    void info(){

        System.out.println(
            "___________________"
            +
            "\n"
            +
            "NOMBRE: " + nombre
            +
            "\n"
            +
            "ATAQUE: " + ataque +
            "\n"
            +
            "VIDA: " + vida +
            "\n"
            +
            "ESTADO: " + estado
            +
            "\n"
            +
            "___________________"

        );
    }

    boolean estarVivo(){

        if (vida > 0){
            return true;
        }
        else {
            return false;
        }
        
    }

}
