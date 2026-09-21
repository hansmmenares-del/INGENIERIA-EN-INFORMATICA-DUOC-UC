public class Atun extends Pez {
    int velocidadNado;
    public Atun(
            String nombre,
            double peso,
            double longitud,
            int velocidadNado) {
        super(
                nombre,
                peso,
                longitud);
        this.velocidadNado = velocidadNado;
    }

    @Override
    public void info(Pez pez) {
        super.info(pez);
        System.out.println(
            "VELOCIDAD DE NADO: ");
    }
    @Override
    public void sonido(Pez pez) {
        super.sonido(pez);
    }
}