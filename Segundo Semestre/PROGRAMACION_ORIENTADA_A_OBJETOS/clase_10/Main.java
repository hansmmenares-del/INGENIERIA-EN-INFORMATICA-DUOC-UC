public class Main {
    public static void main(String[] args){
        System.out.println("\n\nHOLA\n\n");
        
        
        Animal perro = null;
            try {
                perro.hacersonido();
            }
            catch(NullPointerException e) {
                System.out.println("ANIMAL NO INICIALIZADO");
            }
    }
    class Animal{
        String nombre;
        public Animal(String nombre) {
            this.nombre = nombre;
        }
        public void hacersonido(){
            System.out.println("HOLA");
        }
    }
}
