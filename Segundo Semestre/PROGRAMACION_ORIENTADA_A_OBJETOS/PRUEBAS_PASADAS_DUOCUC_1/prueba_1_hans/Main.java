public class Main {
    public static void main(String[] args) {

    Pasajero pasajero1 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");
    Pasajero pasajero2 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");
    Pasajero pasajero3 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");
    Pasajero pasajero4 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");
    Pasajero pasajero5 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");
    Pasajero pasajero6 = new Pasajero("primerNombre", "segundoNombre", "apellidoPaterno", "apellidoMaterno", "rut", "fechaDeNacimiento", "numVisa", pasaporte, "correo");

    PaqueteTuristico paquete1 = new PaqueteNacional(
        pasajero1, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");
    PaqueteTuristico paquete2 = new PaqueteInternacional(
        pasajero2, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");
    PaqueteCrucero paquete3 = new PaqueteCrucero(
        pasajero3, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");
    PaqueteNacional paquete4 = new PaqueteNacional(
        pasajero4, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");
    PaqueteInternacional paquete5 = new PaqueteInternacional(
        pasajero5, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");
    PaqueteCrucero paquete6 = new PaqueteCrucero(
        pasajero6, "duracionEnDias", "fechaDeIda", "fechaDeVuelta");


    }
}