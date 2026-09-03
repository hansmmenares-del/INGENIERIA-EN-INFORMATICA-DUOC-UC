public class Main {
    public static void main(String[] args) {

        // CREACIÓN DE PERSONAJES

        Mounstro mounstro_1 = new Mounstro(

            "Gorgath",
            10,
            250,
            "Vivo"
        );
        Mago mago_1 = new Mago(
            "Merlín",
            15,
            80,
            "Vivo",
            8
        );
        Sanador sanador_1 = new Sanador(
            "Lunara",
            5,
            120,
            "Vivo",
            4
        );
        Arquero arquero_1 = new Arquero(
            "Legolas",
            12,
            90,
            "Vivo",
            "alto"
        );
        Guerrero guerrero_1 = new Guerrero(
            "Thorgar",
            20,
            150,
            "Vivo"
        );

        // ESTADO INICIAL

        System.out.println("\n==============================\nESTADO INICIAL\n==============================");

        mounstro_1.info();
        guerrero_1.info();
        sanador_1.info();
        arquero_1.info();
        mago_1.info();

        System.out.println("\n==============================\nTURNO 1\n==============================\n");

        System.out.println("Merlín ataca a Gorgath:");

        mago_1.relampago(mounstro_1);

        mounstro_1.info();

        System.out.println("\n==============================");
        System.out.println("         TURNO 2");
        System.out.println("==============================\n");

        System.out.println("Legolas utiliza Flecha Triple:");

        arquero_1.flechaTriple(mounstro_1);

        mounstro_1.info();

        System.out.println("\n==============================");
        System.out.println("         TURNO 3");
        System.out.println("==============================\n");

        System.out.println("\nGorgath envenena a Legolas:");

        mounstro_1.envenenar(arquero_1);

        arquero_1.info();

        System.out.println("\n==============================");
        System.out.println("         TURNO 4");
        System.out.println("==============================\n");

        System.out.println("\nLunara cura el estado de Legolas:");

        sanador_1.curar(arquero_1);

        arquero_1.info();

        System.out.println("\n==============================");
        System.out.println("         TURNO 5");
        System.out.println("==============================");

        System.out.println("\nMerlín ataca accidentalmente a Thorgar:");

        mago_1.ventisca(guerrero_1);

        guerrero_1.info();


        // ================================
        // TURNO 6
        // EL ARQUERO ATACA AL MAGO
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 6");
        System.out.println("==============================");

        System.out.println("\nLegolas responde atacando a Merlín:");

        arquero_1.flechaTriple(mago_1);

        mago_1.info();


        // ================================
        // TURNO 7
        // EL MONSTRUO ATACA AL MAGO
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 7");
        System.out.println("==============================");

        System.out.println("\nGorgath envenena a Merlín:");

        mounstro_1.envenenar(mago_1);

        mago_1.info();


        // ================================
        // TURNO 8
        // SANADOR CURA AL MAGO
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 8");
        System.out.println("==============================");

        System.out.println("\nLunara cura a Merlín:");

        sanador_1.curar(mago_1);

        mago_1.info();


        // ================================
        // TURNO 9
        // EL MAGO USA SU ATAQUE FUERTE
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 9");
        System.out.println("==============================");

        System.out.println("\nMerlín utiliza Ventisca contra Gorgath:");

        mago_1.ventisca(mounstro_1);

        mounstro_1.info();


        // ================================
        // TURNO 10
        // EL GUERRERO INTENTA SU HABILIDAD
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 10");
        System.out.println("==============================");

        System.out.println("\nThorgar utiliza Golpe Justicia:");

        guerrero_1.golpeJusticia(mounstro_1);


        // ================================
        // TURNO 11
        // EL MONSTRUO ATACA AL GUERRERO
        // ================================

        System.out.println("\n==============================");
        System.out.println("         TURNO 11");
        System.out.println("==============================");

        System.out.println("\nGorgath utiliza Golpe Mortal contra Thorgar:");

        mounstro_1.golpeMortal(guerrero_1);

        guerrero_1.info();


        // ================================
        // TURNO 12
        // TODOS CONTRA EL MONSTRUO
        // ================================

        System.out.println("\n==============================");
        System.out.println("    ATAQUE COORDINADO");
        System.out.println("==============================");

        System.out.println("\nMerlín ataca:");
        mago_1.relampago(mounstro_1);

        System.out.println("\nLegolas ataca:");
        arquero_1.flechaTriple(mounstro_1);

        System.out.println("\nThorgar ataca:");
        guerrero_1.golpeJusticia(mounstro_1);


        // ================================
        // ESTADO FINAL
        // ================================

        System.out.println("\n==============================");
        System.out.println("       ESTADO FINAL");
        System.out.println("==============================");

        mounstro_1.info();
        mago_1.info();
        sanador_1.info();
        arquero_1.info();
        guerrero_1.info();
    }
}