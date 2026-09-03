public class MiembroVIP extends Miembro{
    public MiembroVIP(String nombre, int edad, boolean mensualidadPagada, Entrenador entrenadorAsignado){
        super(nombre, edad, mensualidadPagada, entrenadorAsignado);
    }
    @Override
    void mostrarInformacion(){
        System.out.println("QUE COOOOL!!!");
    }
}
