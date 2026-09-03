public class Main{
    public static class Animal {
        public String name;
        private int age;
        public Animal(String name, int age) {
            this.name = name;
            this.age = age;
        }
        public void hacerSonido(){
            System.out.println(name + " hace sonido generico");
        }
        public void info(){
            System.out.println(name + " " + age);
        }
        public static class Perro extends Animal{
            public Perro(String name, int age){
                super(name, age);
            }
        @Override
        public void hacerSonido(){
            System.out.println(name + " ladra! WOF WOF");
            }
        }
        public static class Gato extends Animal{
            public Gato(String name, int age){
                super(name, age);
            }
            @Override
            public void hacerSonido(){
                System.out.println(name + " maulla! MIAU MIAU");
            }
        }
    public static void main(String[] args) {
        Animal toby = new Animal("Perro", 2);
        Animal cachupin = new Animal("Mufasa", 12);
        cachupin.info();
        toby.info();
        Perro perro1 = new Perro("perro1", 3);
        perro1.info();
        perro1.hacerSonido();
        Gato gato1 = new Gato("michi", 5);
        gato1.info();
        gato1.hacerSonido();
        }
    }
}