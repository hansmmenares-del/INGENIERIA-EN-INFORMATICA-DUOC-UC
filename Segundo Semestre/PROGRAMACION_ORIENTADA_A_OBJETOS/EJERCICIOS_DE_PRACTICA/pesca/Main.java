import peces.Atun;
import peces.Pez;
import peces.Robalo;
import peces.Salmon;

public class Main {
    public static void main(String[] args) {

        System.out.println("--------");

        Pescador pescador1 = null;
        try {
            pescador1 = new Pescador(
                "CHILE",
                "HANS",
                35
            );
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pescador pescador2 = null;
        try {
            pescador2 = new Pescador(
                "HAITI",
                "JEFFREY Ep.",
                58
            );
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez1 = null;
        try {
            pez1 = new Atun(
                "nombre_pez",
                9.0,
                100, 5
            );
            pez1.info();
            System.out.println(pez1.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez2 = null;
        try {
            pez2 = new Atun(
                "nombre_pez",
                9.0,
                100, 0
            );
            pez2.info();
            System.out.println(pez2.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez3 = null;
        try {
            pez3 = new Atun(
                "nombre_pez",
                9.0,
                100, 0
            );
            pez3.info();
            System.out.println(pez3.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez4 = null;
        try {
            pez4 = new Salmon(
                "nombre_pez",
                9.0,
                100, null
            );
            pez4.info();
            System.out.println(pez4.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez5 = null;
        try {
            pez5 = new Salmon(
                "nombre_pez",
                9.0,
                100, null
            );
            pez5.info();
            System.out.println(pez5.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez6 = null;
        try {
            pez6 = new Salmon(
                "nombre_pez",
                9.0,
                100, null
            );
            pez6.info();
            System.out.println(pez6.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez7 = null;
        try {
            pez7 = new Robalo(
                "nombre_pez",
                9.0,
                100, 0
            );
            pez7.info();
            System.out.println(pez7.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez8 = null;
        try {
            pez8 = new Robalo(
                "nombre_pez",
                9.0,
                100, 0
            );
            pez8.info();
            System.out.println(pez8.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Pez pez9 = null;
        try {
            pez9 = new Robalo(
                "nombre_pez",
                9.0,
                100, 0
            );
            pez9.info();
            System.out.println(pez9.sonido());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        if (pescador1 != null) {
            try{
                pescador1.pescar(pez1);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try{
                pescador1.pescar(pez2);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try{
                pescador1.pescar(pez3);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try{
                pescador1.pescar(pez4);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try{
                pescador1.pescar(pez5);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try{
                pescador1.mostrarPeces();
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("\n\nPescador 1 no existe\n\n");
        }
        if (pescador2 != null){
            try {
                pescador2.pescar(pez6);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try {
                pescador2.pescar(pez7);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try {
                pescador2.pescar(pez8);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try {
                pescador2.pescar(pez9);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
            try {
                pescador2.mostrarPeces();
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("\n\nPescador 2 no existe\n\n");
        }
    }
}