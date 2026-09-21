public class ChicaLinda {

    private String nombre;
    private int nivelDeHermosura;

    ChicaLinda(String nombre, int nivelDeHermosura) {

        this.nombre = nombre;
        this.nivelDeHermosura = nivelDeHermosura;

    }

    public String getNombre(ChicaLinda chicaLinda) {
        return this.nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int nivelDeHermosura(ChicaLinda chicaLinda) {
        return this.nivelDeHermosura;
    }
    public void setNivelDeHermosura(int nivelDeHermosura) {
        this.nivelDeHermosura = nivelDeHermosura;
    }

}