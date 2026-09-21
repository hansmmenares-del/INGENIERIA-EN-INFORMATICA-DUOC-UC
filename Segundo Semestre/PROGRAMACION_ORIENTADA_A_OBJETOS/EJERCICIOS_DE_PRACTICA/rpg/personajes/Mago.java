package personajes;
import interfaces.AtaquesBasicos;
public class Mago extends Personaje implements AtaquesBasicos{
    
    private double magia;

    public Mago(
        List<HechizosMagia> hechizosEnPersonaje
    ) throws Exception {
        super(nombre, edad, ataque, vida, stamina, charisma, hechizosEnPersonaje);
        if (magia <= 0) {
            throw new IllegalArgumentException("");
        }
        this.magia = magia;
    }

    @Override
    public void ataqueBasico(Personaje enemigo) throws Exception {
        if (ataque <= 0) {
            throw new NullPointerException();
        } else {
            enemigo.get
        }
    }
    public double getMagia() {
        return magia;
    }
    public void setMagia(double magia) throws Exception {
        if (magia <= 0) {
            throw new IllegalArgumentException("");
        }
        this.magia = magia;
    }
}