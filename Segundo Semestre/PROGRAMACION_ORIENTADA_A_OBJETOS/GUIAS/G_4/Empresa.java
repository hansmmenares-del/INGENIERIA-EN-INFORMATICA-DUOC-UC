public class Empresa {

    String nombreEmpresa;
    Empleado gerente;
    Empleado vendedor1;
    Empleado vendedor2;

    Empresa(String nombreEmpresa, Empleado gerente, Empleado vendedor1, Empleado vendedor2) {

        this.nombreEmpresa = nombreEmpresa;
        this.gerente = gerente;
        this.vendedor1 = vendedor1;
        this.vendedor2 = vendedor2;

    }

    public void calcularNominaTotal() {

        double calculo_interno = gerente.calcularSueldo() + vendedor1.calcularSueldo() + vendedor2.calcularSueldo();
        System.out.println("CALCULO DE NOMINA TOTAL: $" + calculo_interno);

    }

    public void mostratNomina() {

        gerente.mostrarInformacion();
        vendedor1.mostrarInformacion();
        vendedor2.mostrarInformacion();
        
    }
}
