public class Animales {
    
    String nombre;
    private int edad;
    private double peso;
    
    public Animales(String nombre, int edad, double peso){
        this.nombre = nombre;
        this.edad = edad;
        this.peso = peso;
    }

    public Animales() {
        this.nombre = "Desconocido";
        this.edad = 0;
        this.peso = 0;
    }

    public void getInfo(){
        System.out.println(this.nombre + " " + this.edad + " " + this.peso);
    }

    public int getEdad(){
        return this.edad;
    }
    public double getPeso(){
        return this.peso;
    }
}
