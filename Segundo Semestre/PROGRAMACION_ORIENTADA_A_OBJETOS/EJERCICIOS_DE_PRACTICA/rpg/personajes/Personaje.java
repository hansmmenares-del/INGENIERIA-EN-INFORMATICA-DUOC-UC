package personajes;
import interfaces.HechizosMagia;
import java.util.ArrayList;
import java.util.List;

public abstract class Personaje {

    private String nombre;
    private int edad;
    private double ataque;
    private double vida;
    private double stamina;
    private double charmisma;
    private List<HechizosMagia> hechizosEnPersonaje;

    public Personaje(

        String nombre,
        int edad,
        double ataque,
        double vida,
        double stamina,
        double charmisma,
        List<HechizosMagia> hechizosEnPersonaje

    ) throws Exception {

        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("");
        }
        if (edad <= 0) {
            throw new IllegalArgumentException("");
        }
        if (vida <= 0) {
            throw new IllegalArgumentException("");
        }
        if (stamina <= 0) {
            throw new IllegalArgumentException("");
        }
        if (charmisma <= 0) {
            throw new IllegalArgumentException("");
        }

        this.nombre = nombre;
        this.edad = edad;
        this.ataque = ataque;
        this.vida = vida;
        this.stamina = stamina;
        this.charmisma = charmisma;
        this.hechizosEnPersonaje = new ArrayList<>();
    }

    public String getNombre() {
        return this.nombre;
    }
    public int getEdad() {
        return this.edad;
    }
    public double getAtaque() {
        return this.ataque;
    }
    public double getVida() {
        return this.vida;
    }
    public double getStamina() {
        return this.stamina;
    }
    public double getCharmisma() {
        return this.charmisma;
    }
    public List<HechizosMagia> getHechizosEnPersonaje() {
        return this.hechizosEnPersonaje;
    }

    public void setNombre(String nombre) throws Exception {
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException(eIlegalArgExcept_nombre());
        }
    }
    public void setEdad(int edad) throws Exception {
        if (edad <= 0) {
            throw new IllegalArgumentException(eIlegalArgExcept_edad());
        }
    }
    public void setAtaque(double ataque) throws Exception {
        if (ataque == 0) {
            throw new IllegalAccessException(eIlegalArgExcept_ataque());
        }
    }
    public void setVida(double vida) throws Exception {
        if (vida <= 0) {
            throw new IllegalArgumentException(eIlegalArgExcept_vida());
        }
    }
    public void setStamina(double stamina) throws Exception {
        if (stamina <= 0) {
            throw new IllegalArgumentException(eIlegalArgExcept_stamina());
        }
    }
    public void setCharmisma(double charisma) throws Exception {
        if (charmisma <= 0) {
            throw new IllegalArgumentException(eIlegalArgExcept_charmisma());
        }
    }

    private String eIlegalArgExcept_nombre () {
        return " ";
    }
    private String eIlegalArgExcept_edad () {
        return " ";
    }
    private String eIlegalArgExcept_ataque () {
        return " ";
    }
    private String eIlegalArgExcept_vida () {
        return " ";
    }
    private String eIlegalArgExcept_stamina () {
        return " ";
    }
    private String eIlegalArgExcept_charmisma () {
        return " ";
    }
}