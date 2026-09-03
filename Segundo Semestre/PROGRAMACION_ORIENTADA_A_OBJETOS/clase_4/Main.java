
public class Main {
    public static void main(String[] args){

        Persona persona_1 = new Persona(30, 1.75, "Juan Perez");

        persona_1.saludar("Hans");

    }
    public static class Persona{

        // ATRIBUTES
        private int age;
        private double height;
        private String name;

        // CONSTRUCTOR
        public Persona(int age, double height, String name){
            this.age = age;
            this.height = height;
            this.name = name;
        }

        // METHODS
        public void saludar(String nombreQuienSaluda){
            System.out.println("Hola " + nombreQuienSaluda);
        }
    }
}

// public [tipo][nombre]([argumentos]){[codigo]}public 
// CLASE; PARAMETROS; METODOS; CREACION; ABS; HEREN; POLIMORF; 