import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner entrada = new Scanner(System.in);
    static ArrayList<PaqueteTuristico> paquetes = new ArrayList<>();
    static double impuesto = 0;

    public static void main(String[] args) {

        System.out.println("Ingresa el porcentaje de impuesto (0 a 100): ");
        impuesto = Double.parseDouble(entrada.nextLine());

        int opcion = 0;

        while (opcion != 7){
            System.out.println("============================================\n" +
                    "AGENCIA DE VIAJES VOYAGETOP\n" +
                    "============================================");
            System.out.println("1. Registrar paquete");
            System.out.println("2. Listar paquetes");
            System.out.println("3. Buscar por destino");
            System.out.println("4. Buscar por destino y tipo");
            System.out.println("5. Contratar seguro");
            System.out.println("6. Consultar seguro");
            System.out.println("0. Salir");

            try{
                opcion = leerEntero("Selecciona una opción: ");

                switch (opcion){
                    case 1:
                        registrarPaquete();
                        break;
                    case 2:
                        listarPaquetes();
                        break;
                    case 3:
                        buscarPorDestino();
                        break;
                    case 4:
                        buscarPorDestinoYTipo();
                        break;
                    case 5:
                        contratarSeguro();
                        break;
                    case 6:
                        consultarSeguro();
                        break;
                    case 7:
                        System.out.println("Programa finalizado");
                        break;
                    default:
                        System.out.println("Opción no válida");

                }
            }catch (Exception error){
                System.out.println("Error: " + error.getMessage());
            }
        }

        entrada.close();
    }

    static void registrarPaquete(){

        System.out.println("Ingresa el nombre del Pasajero: ");
        String nombre = entrada.nextLine().trim();

        System.out.println("Ingresa el pasaporte o RUT: ");
        String pasaporte = entrada.nextLine().trim();

        System.out.println("Ingresa el correo del Pasajero: ");
        String correo = entrada.nextLine().trim();

        Pasajero pasajero = new Pasajero(nombre, pasaporte, correo);

        System.out.println("Ingresa el destino del viaje: ");
        String destino = entrada.nextLine().trim();

        int duracion = leerEntero("ingresa la cantidad de días");

        System.out.println("1. Paquete Nacional");
        System.out.println("2. Paquete Internacional");
        System.out.println("3. Paquete Crucero");

        int tipo = leerEntero("Selecciona el tipo de paquete");

        PaqueteTuristico paquete;

        if (tipo == 1){
            paquete = new PaqueteNacional(destino, duracion, pasajero);
        } else if (tipo == 2) {
            System.out.println("¿Es en primera clase? (s/n): ");
            String resp = entrada.nextLine().trim();
            Boolean primeraClase = resp.equalsIgnoreCase("s");
            paquete = new PaqueteInternacional(destino, duracion, pasajero, primeraClase);
        } else if (tipo == 3) {
            System.out.println("¿Camarote incluye balcón? (s/n): ");
            String resp = entrada.nextLine().trim();
            Boolean conBalcon = resp.equalsIgnoreCase("s");
            paquete = new PaqueteCrucero(destino, duracion, pasajero, conBalcon);
        } else {
            throw new IllegalArgumentException("El tipo de paquete debe ser 1, 2 o 3.");
        }

        paquetes.add(paquete);
        System.out.println("Paquete registrado exitosamente");
    }

    static void listarPaquetes(){

        if(paquetes.isEmpty()){
            System.out.println("No existen paquetes registrados");
            return;
        }

        for (PaqueteTuristico paquete : paquetes){
            System.out.println("Destino: " + paquete.getDestino() + " | Días: " + paquete.getDuracion());
            System.out.println("Tipo: " + paquete.getTipo() + " | Costo base: $" + paquete.calcularCosto() + " | Total final: $" + paquete.calcularPrecioFinal(impuesto));
            System.out.println("Pasajero: " + paquete.getPasajero().getNombre());
            if (paquete instanceof Asegurable) {
                Asegurable aseg = (Asegurable) paquete;
                System.out.println("Estado Seguro: " + aseg.consultarSeguro());
            }
            System.out.println("---------------------------");
        }
    }
    static void buscar(String destino){
        boolean encontro = false;
        for (PaqueteTuristico p : paquetes) {
            if (p.getDestino().equalsIgnoreCase(destino)) {
                System.out.println("Encontrado: " + p.getDestino() + " | " + p.getTipo() + " | Pasajero: " + p.getPasajero().getNombre());
                encontro = true;
            }
        }
        if (!encontro) {
            System.out.println("No se encontró paquete para ese destino");
        }
    }
    static void buscar(String destino, String tipo){
        boolean encontro = false;
        for (PaqueteTuristico p : paquetes) {
            if (p.getDestino().equalsIgnoreCase(destino) && p.getTipo().equalsIgnoreCase(tipo)) {
                System.out.println("Encontrado: " + p.getDestino() + " | " + p.getTipo() + " | Pasajero: " + p.getPasajero().getNombre());
                encontro = true;
            }
        }
        if (!encontro) {
            System.out.println("No se encontró paquete para ese destino y tipo");
        }
    }
    static void buscarPorDestino(){
        System.out.println("Ingresa el destino a buscar: ");
        String destino = entrada.nextLine().trim();
        buscar(destino);
    }
    static void buscarPorDestinoYTipo(){
        System.out.println("Ingresa el destino a buscar: ");
        String destino = entrada.nextLine().trim();

        System.out.println("1. Paquete Nacional");
        System.out.println("2. Paquete Internacional");
        System.out.println("3. Paquete Crucero");
        int t = leerEntero("Selecciona el tipo");

        String tipo = "";
        if (t == 1) tipo = "Paquete Nacional";
        if (t == 2) tipo = "Paquete Internacional";
        if (t == 3) tipo = "Paquete Crucero";

        buscar(destino, tipo);
    }

    static void contratarSeguro(){
        System.out.println("Ingresa el destino del paquete internacional: ");
        String destino = entrada.nextLine().trim();

        for (PaqueteTuristico p : paquetes) {
            if (p.getDestino().equalsIgnoreCase(destino) && p instanceof Asegurable) {
                System.out.println("Ingresa el nombre de la compañía aseguradora: ");
                String compania = entrada.nextLine().trim();

                Asegurable aseg = (Asegurable) p;
                System.out.println(aseg.contratarSeguro(compania));
                return;
            }
        }
        System.out.println("No se encontró paquete internacional con ese destino");
    }

    static void consultarSeguro(){
        System.out.println("Ingresa el destino del paquete internacional: ");
        String destino = entrada.nextLine().trim();

        for (PaqueteTuristico p : paquetes) {
            if (p.getDestino().equalsIgnoreCase(destino) && p instanceof Asegurable) {
                Asegurable aseg = (Asegurable) p;
                System.out.println("Estado del seguro: " + aseg.consultarSeguro());
                return;
            }
        }
        System.out.println("No se encontró paquete internacional con ese destino");
    }
    static int leerEntero(String mensaje){
        System.out.println(mensaje);
        return Integer.parseInt(entrada.nextLine());
    }
}