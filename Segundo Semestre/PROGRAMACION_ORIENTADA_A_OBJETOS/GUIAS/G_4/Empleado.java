public class Empleado {

    public String nombre;
    public double sueldoBase;

    Empleado(String nombre, double suledoBase) {

        this.nombre = nombre;
        this.sueldoBase = suledoBase;

    }

    public double calcularSueldo() {

        return this.sueldoBase;

    }

    public double calcularSuledo() {

        return this.sueldoBase;

    }

    public void mostrarInformacion() {

        System.out.println("NOMBRE: " + this.nombre
            +
            "\n"
            +
            "SUELDO CALCULADO: " + calcularSueldo());
            
    }
}
