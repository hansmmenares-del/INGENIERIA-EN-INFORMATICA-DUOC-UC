public class Mago extends Personaje {
    
    double magia;

    Mago(String nombre,
        double ataque,
        double vida,
        String estado,
        double magia) {
        super(nombre, ataque, vida, estado);
        this.magia = magia;
    }

    void relampago(Personaje enemigo) {

        double ataque = 1.5 * magia;
        enemigo.vida -= ataque;

        System.out.println(
            "El ataque de relampago inflige " + ataque + " puntos de daño a " + enemigo.nombre + "!!!"
        );

    }

    void ventisca(Personaje enemigo){

        double ataque = 3.0 * magia;
        enemigo.vida -= ataque;

        System.out.println(
            "El ataque de ventisca inflige " + ataque + " puntos de daño a " + enemigo.nombre + "!!!"
        );

    }
}