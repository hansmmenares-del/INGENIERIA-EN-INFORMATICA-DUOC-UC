
import java.util.*;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {

        Perro perro1 = new Perro("aa", 0, 0);
        Perro perro2 = new Perro("bb", 6, 0);
        Perro perro3 = new Perro("cc", 0, 0);
        Perro perro4 = new Perro("dd", 9, 0);
        Gato gato1 = new Gato("ab", 0, 0);
        Gato gato2 = new Gato("ac", 0, 0);
        Gato gato3 = new Gato("ad", 0, 0);
        Pato pato1 = new Pato("ba", 0, 0);
        Pato pato2 = new Pato("bc", 0, 0);
        Pato pato3 = new Pato("bd", 0, 0);
        List <Animal> listaAnimales = new ArrayList<>();
        listaAnimales.add(perro1);
        listaAnimales.add(perro2);
        listaAnimales.add(perro3);
        listaAnimales.add(gato1);
        listaAnimales.add(gato2);
        listaAnimales.add(gato3);
        listaAnimales.add(pato1);



        listaAnimales.get(0);
        listaAnimales.remove(0);
        listaAnimales.size();

        Map<String, Animal> zoo = new HashMap <String,Animal>();
        zoo.put("perro", perro1);
        zoo.put("gato", gato1);
        zoo.put("pato", pato1);

        zoo.get("perro1");


        List<Animal> listaDeCosas = new ArrayList<>();
        Map<String, Animal> mapDeCosas = new HashMap<>();



        List<Integer> listaDeNumeros = new ArrayList<>();
        listaDeNumeros.add(1);
        listaDeNumeros.add(2);
        listaDeNumeros.add(3);
        listaDeNumeros.add(4);

        for (int numero: listaDeNumeros){
            if (numero == 2) {
                System.out.println(numero);
            }
        }
        Map<String, Integer> mapaDeNumeros = new HashMap<>();
        mapaDeNumeros.put("a", 1);
        mapaDeNumeros.put("b", 2);
        mapaDeNumeros.put("c", 3);
        mapaDeNumeros.put("d", 4);




        for (Animal animal: listaAnimales) {
            System.out.println(
                "NOMBRE: " + animal.nombre
                +
                "\n"
                +
                "EDAD: " + animal.edad
                +
                "\n"
                +
                "PESO: " + animal.peso
            );
            if (animal.edad >= 3) {
                System.out.println("---ANZIANO---");
            }
            else {
                System.out.println("---67---");

            }
        }

        for (Map.Entry <String, Animal> animalito : zoo.entrySet()) {

            String clave = animalito.getKey();
            Animal animal = animalito.getValue();

            System.out.println(
                "CLAVE: " + clave
                +
                "\n"
                +
                "NOMBRE: " + animal.nombre
            );
        }



        // EXCEPCIONES
        
    }
}