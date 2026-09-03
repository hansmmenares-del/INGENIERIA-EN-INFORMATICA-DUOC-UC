public class Guerrero extends Personaje {
    Guerrero(String nombre,
        double ataque,
        double vida,
        String estado) {

        super(nombre, ataque, vida, estado);

    }

    void golpeJusticia(Mounstro mounstro) {

        if (Math.random() >= 0.4) {
            
            System.out.println(this.nombre + " ha bloqueado con exito el ataque de " + mounstro.nombre);

        }
        else if (Math.random() < 0.4){
            System.out.println("Ataque evadido por " + mounstro.nombre);
        }

    }
    void bloqueo(){
        // inflige 2.2 * ataque puntos de daño.
        
    }

}