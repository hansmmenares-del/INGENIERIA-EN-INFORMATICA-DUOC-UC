import java.util.Scanner;
public class Main {
public static class Animal{
        // Atributos Animal
        String name = "Perro";
        int age;
        int timesHasEaten = 0;

        public void makeSound(String name){
            System.out.println("WOF !!!");
            System.out.println(name + " has talked\n\n");
        }
        public void comer(String name){
            System.out.println("ñom ñom");
            System.out.println(name + " has eaten!\n\n");
        }
        public int opc_usuario(Scanner scanner){
            System.out.println("(1) Make Sound.\n(2) Give Food.\nSelect an option: ");
            int opc = scanner.nextInt();
            return opc;
        }
    }

    public static class Human{
        String name;
        int amountOfMaracas;

        public Human(String name, int amountOfMaracas){
            this.name = name;
            this.amountOfMaracas = amountOfMaracas;
        }
    }
    public static void main(String args[]){

        Human renato = new Human("Renato", 4);


        Scanner scanner_animal = new Scanner(System.in);
        Animal animal = new Animal();
        while (true) {
            
            int opc = animal.opc_usuario(scanner_animal);

            if (opc == 1) {
                animal.makeSound(animal.name);
            }
            else if (opc == 2) {
                animal.comer(animal.name);
                }
            else if (opc == 3){
                System.out.println("|| CREANDO HUMANO ||");
                System.out.println("Ingresa el nombre del individuo: ");

                
            }
        }
    }
}
