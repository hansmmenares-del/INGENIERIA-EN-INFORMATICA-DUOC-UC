public class Mounstro extends Personaje {
    
    Mounstro(String nombre,
        double ataque,
        double vida,
        String estado) {

        super(nombre, ataque, vida, estado);

    }

    void envenenar(Personaje enemigo) {

        enemigo.vida -= ataque;
        enemigo.estado = "Envenenado";
        System.out.println(this.nombre + " ha atacado " + "(-" + ataque + ") y envenenado a " + enemigo.nombre + "!!!");

    }

    void golpeMortal(Personaje enemigo) {
        
        if (enemigo.vida < 50) {
            enemigo.vida = 0;
            enemigo.estado = "Desmayado";

            System.out.println(this.nombre + " ha atacado " + "(-" + ataque + ") y ha derrotado a " + enemigo.nombre + "!!!");

        }

        else if (enemigo.vida >= 50){

            enemigo.vida -= 5 * ataque;

            System.out.println(this.nombre + " ha atacado " + "(-" + (5 * ataque) + ") a " + enemigo.nombre + "!!!");
        }
    }
}
