public class Arquero extends Personaje {
    String rango;
    Arquero(String nombre, double ataque, double vida, String estado, String rango) {
        super(nombre, ataque, vida, estado);
        this.rango = rango;
    }
    void flechaTriple(Personaje enemigo) {
        if (rango == "bajo") {
            double daño = 1 * ataque;
            enemigo.vida -= daño;
        } else if (rango == "medio") {
            double daño = 2 * ataque;
            enemigo.vida -= daño;
        } else if (rango == "alto") {
            double daño = 3 * ataque;
            enemigo.vida -= daño;
        } else {
            System.out.println("Rango no valido");
        }
    }

}