public class Gerente extends Empleado {

    double bono;

    Gerente(String nombre, double sueldoBase, double bono){

        super(nombre, sueldoBase);
        this.bono = bono;     
    
    }

    @Override
    public double calcularSueldo() {

        return this.sueldoBase + this.bono;
        
    }
}
