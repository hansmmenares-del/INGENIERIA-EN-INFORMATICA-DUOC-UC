
import personajes.Mago;

import java.util.ArrayList;
import java.util.List;

import personajes.Arquero;
import personajes.Guerrero;
import personajes.Mounstro;
import personajes.Sanador;

import personajes.Personaje;
public class Main {
    public static void main(String[] args) {

        Personaje personaje1 = new Mago("hans", 2, 3, 4);
        Personaje personaje2 = new Mago(null, 0, 0, 0);
        Personaje personaje3 = new Sanador();
        Personaje personaje4 = new Arquero(null, null, 0, 0, 0, 0, 0, null);
        Personaje personaje5 = new Guerrero();
        Personaje personaje6 = new Guerrero();
        Personaje personaje7 = new Mounstro();
        Personaje personaje8 = new Sanador();

    }
}