public class Sanador extends Personaje {
    double magia;
    Sanador(String nombre, double ataque, double vida, String estado, double magia) {
        super(nombre, ataque, vida, estado);
        this.magia = magia;
    }

    void sanar(Personaje aliado){

        aliado.vida += magia;

        System.out.println(this.nombre + " ha sanado a " + aliado.nombre + " recuperando " + magia + " puntos de vida");

    }

    void curar(Personaje aliado){

        aliado.estado = "Sano";

        System.out.println(this.nombre + " ha curado a " + aliado.nombre + ". Su estado ahora es Sano.");

    }

    void curar(){

        this.estado = "Sano";
        
        System.out.println(this.nombre + " se ha sanado a si mismo. Su estado ahora es Sano.");

    }

    void bendecir(Personaje aliado){

        aliado.ataque += 10;

        System.out.println(this.nombre + " ha bendecido a " + aliado.nombre + ". Su ataque aumenta 10 puntos.");

    }
}