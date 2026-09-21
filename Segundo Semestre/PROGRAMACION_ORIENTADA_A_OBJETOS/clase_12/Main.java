import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Pez pez1 = new Pez("pecesillo 1", 10, 40);
        Pez pez2 = new Pez("pecesillo 2", 17, 50);
        Pez pez3 = new Pez("pecesillo 3", 16, 60);
        Pez pez4 = new Pez("pecesillo 4", 13, 70);
        Pez pez5 = new Pez("pecesillo 5", 15, 80);
        Pez pez6 = new Pez(null, 0, 0);
        Pez pez7 = new Pez(null, 0, -1);
        Pez pez8 = new Pez(null, -1, 0);
        Pez pez9 = new Pez("errorProneFish", -1, -1);

        Pescador pescador1 = new Pescador("Juan", 30, "Haitiano");
        Pescador pescador2 = new Pescador("Juan", 30, "Judio");

        pez1.info(pez1);
        pez2.info(pez2);
        pez3.info(pez3);
        pez4.info(pez4);
        pez5.info(pez5);
        pescador1.pescarPez(pez1, pescador1);
        pescador2.pescarPez(pez2, pescador2);
        pescador2.pescarPez(pez3, pescador2);
        pescador1.pescarPez(pez4, pescador1);

        pescador1.mostrarPeces();

        // ChicaLinda chicaMasHermosa = new ChicaLinda("GUS", 100);
        // System.out.println(
        //     "\n\n\n"
        //     +
        //     "Estoy todo loco por usted mi gatita llamada: "
        //     +
        //     chicaMasHermosa.getNombre(chicaMasHermosa)
        //     +
        //     "\n"
        //     +
        //     "Besemonos? jeje con agarron sipo si no pa ke"
        //     +
        //     "\n\n\n"
        // );
    }
}
