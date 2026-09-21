import jugadores.Jugador;

import java.util.ArrayList;
import java.util.List;

import jugadores.Arquero;
import jugadores.Defensor;
import jugadores.MedioCampista;
import jugadores.Delantero;

public class Main {
    public static void main(String[] args) {

        Jugador jugador1 = null;
        try {
            jugador1 = new Arquero("Gianluigi Buffon", 8.5);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador2 = null;
        try {
            jugador2 = new Defensor("Sergio Ramos", -12.7);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        
        }
        Jugador jugador3 = null;
        try {
            jugador3 = new Defensor(null, 10.4);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador4 = null;
        try {
            jugador4 = new Defensor("Virgil van Dijk", 0);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador5 = null;
        try {
            jugador5 = new MedioCampista("Luka Modric", 18.6);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador6 = null;
        try {
            jugador6 = new MedioCampista("Andres Iniesta", -21.3);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador7 = null;
        try {
            jugador7 = new MedioCampista(null, 16.8);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador8 = null;
        try {
            jugador8 = new MedioCampista("Zinedine Zidane", 25.7);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador9 = null;
        try {
            jugador9 = new Delantero("Lionel Messi", 87.4);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador10 = null;
        try {
            jugador10 = new Delantero("Cristiano Ronaldo", 0);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        Jugador jugador11 = null;
        try {
            jugador11 = new Delantero("Ronaldo Nazario", -82.9);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        if(jugador1 != null) {
            try {
                jugador1.patear(jugador1);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador2 != null) {
            try {
                jugador2.patear(jugador2);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador3 != null) {
            try {
                jugador3.patear(jugador3);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador4 != null) {
            try {
                jugador4.patear(jugador4);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador5 != null) {
            try {
                jugador5.patear(jugador5);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador6 != null) {
            try {
                jugador6.patear(jugador6);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador7 != null) {
            try {
                jugador7.patear(jugador7);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador8 != null) {
            try {
                jugador8.patear(jugador8);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador9 != null) {
            try {
                jugador9.patear(jugador9);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador10 != null) {
            try {
                jugador10.patear(jugador10);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }
            
        if(jugador11 != null) {
            try {
                jugador11.patear(jugador11);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        } else {
            System.out.println("...");
        }


        List<Jugador> listaDeJugadores = new ArrayList<>();

        if (jugador1 != null) {
            listaDeJugadores.add(jugador1);
        }
        if (jugador2 != null) {
            listaDeJugadores.add(jugador2);
        }
        if (jugador3 != null) {
            listaDeJugadores.add(jugador3);
        }
        if (jugador4 != null) {
            listaDeJugadores.add(jugador4);
        }
        if (jugador5 != null) {
            listaDeJugadores.add(jugador5);
        }
        if (jugador6 != null) {
            listaDeJugadores.add(jugador6);
        }
        if (jugador7 != null) {
            listaDeJugadores.add(jugador7);
        }
        if (jugador8 != null) {
            listaDeJugadores.add(jugador8);
        }
        if (jugador9 != null) {
            listaDeJugadores.add(jugador9);
        }
        if (jugador10 != null) {
            listaDeJugadores.add(jugador10);
        }
        if (jugador11 != null) {
            listaDeJugadores.add(jugador11);
        }

        for (Jugador jugador : listaDeJugadores) {
            System.out.println(jugador.getNombre());
        }

        try {
            for (int i = 0; i <= 12 ; i++) {
                System.out.println(listaDeJugadores.get(i).getNombre());
            }
        } catch (IndexOutOfBoundsException e) {
            System.out.println("ERROR FUERA DE LIMITES LOGRADO!");
        }
    }
}
