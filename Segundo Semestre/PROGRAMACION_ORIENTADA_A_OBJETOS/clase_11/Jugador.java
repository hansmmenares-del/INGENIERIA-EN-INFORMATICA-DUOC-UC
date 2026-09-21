public class Jugador {

    String nombre;
    double probabilidadGol;

    public Jugador(
        String nombre,
        double probabilidadGol) {
            this.nombre = nombre;
            this.probabilidadGol = probabilidadGol;
        }
    void patear() throws Exception {
        if (this.nombre == null) {
            throw new NullPointerException("Error: Nombre de jugador es Null");
        }
        if (this.probabilidadGol == 0) {
            throw new ArithmeticException("Error: Probabilidad de jugador fuera de rango(0 a 1)");
        }
        if (this.probabilidadGol < 0 || this.probabilidadGol > 100) {
            throw new ArithmeticException("Error: Probabilidad de jugador fuera de rango (0 a 1)");
        }
        if (probabilidadGol > 50) {
            System.out.println(nombre + " GOOOL!!!");
        }
        else {
            System.out.println(nombre + " FALLO EL PENAL!!");
        }
    }
}