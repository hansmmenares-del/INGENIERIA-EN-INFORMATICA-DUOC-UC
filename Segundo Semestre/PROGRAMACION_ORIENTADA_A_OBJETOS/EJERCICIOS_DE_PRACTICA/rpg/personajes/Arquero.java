package personajes;

import  interfaces.AtaquesArqueros;
import interfaces.AtaquesBasicos;
import interfaces.HechizosMagia;

import java.util.ArrayList;
import java.util.List;

public abstract class Arquero extends Personaje implements AtaquesArqueros, AtaquesBasicos, HechizosMagia
{

    private String rango;

    public Arquero(
        String nombre,
        String rango,
        int edad,
        double ataque,
        double vida,
        double stamina,
        double charmisma,
        List<HechizosMagia> hechizosEnPersonaje,
        List<String> listaDeRangos
    ) throws Exception {
        super(nombre, edad, ataque, vida, stamina, charmisma, hechizosEnPersonaje);
        if (!listaDeRangos.contains(rango)) {
            throw new IllegalArgumentException(e);
        }
        this.rango = rango;
    }

    @Override
    public void ataqueBasico(Personaje enemigo) throws Exception {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'ataqueBasico'");
    }

    @Override
    public void bendicion(Personaje personajeBendice, Personaje personajeBendecido) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'bendicion'");
    }

}