public class Main{
    public static void main(String[] args){
        Entrenador entrenador_1 = new Entrenador("Pedrito", "Reiki", 1);
        
        Entrenador entrenador_2 = new Entrenador("Comy", "Cardio", 3);
        
        Miembro miembro_1 = new Miembro("Hans", 23, false, entrenador_2);
        
        Miembro miembro_2 = new Miembro("kaka", 3, false, entrenador_1);
        
        Miembro miembro_3 = new Miembro("oaoa", 55, false, entrenador_1);

        MiembroVIP miembroVIP_1 = new MiembroVIP("Carlos", 0, false, entrenador_2);
        
        miembro_1.mostrarInformacion();
        miembro_2.mostrarInformacion();
        miembro_3.mostrarInformacion();

        miembroVIP_1.mostrarInformacion();

    }
}