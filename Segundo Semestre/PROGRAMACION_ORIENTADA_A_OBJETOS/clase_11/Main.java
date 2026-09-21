import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {

        Jugador player1 = new Jugador("MessiMessi", -1);
        Jugador player2 = new Jugador("RonaldoCR7", 0);
        Jugador player3 = new Jugador("MBAPEEE", 97);
        Jugador player4 = new Jugador(null, 74);

        List<Jugador> listaDeJugadores = new ArrayList<>();

        listaDeJugadores.add(player1);
        listaDeJugadores.add(player2);
        listaDeJugadores.add(player3);
        listaDeJugadores.add(player4);
        
        for (int i = 0; i < listaDeJugadores.size(); i++) {
            try {
                Jugador jugador = listaDeJugadores.get(i);
                jugador.patear();
            }
            catch (ArithmeticException e) {
            System.out.println("NullPointerException: " + e.getMessage());
            }
            catch (NullPointerException e) {
                System.out.println("NullPointerException: " + e.getMessage());
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("ArrayIndexOutOfBoundsException: " + e.getMessage());
            }
            catch (Exception e) {
                System.out.println("Exception: " + e.getMessage());
            }
            finally {
                System.out.println("\n\n-------- FIN INTENTO --------\n\n");
            }
        }
    }
}