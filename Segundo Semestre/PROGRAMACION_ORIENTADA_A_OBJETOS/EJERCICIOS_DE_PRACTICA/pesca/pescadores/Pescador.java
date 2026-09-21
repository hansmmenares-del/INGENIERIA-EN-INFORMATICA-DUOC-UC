import java.util.ArrayList;
import java.util.List;

import peces.Pez;

public class Pescador {

// ATRIBUTOS
    private List<Pez> listaPecesCapturados = new ArrayList<>();
    private String nacionalidad;
    private String nombre;
    private int edad;

// CONSTRUCTOR
    public Pescador(
        String nacionalidad,
        String nombre,
        int edad
    ) throws Exception {
        if (nacionalidad == null || nacionalidad.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'nacionalidad' no puede ser null ni puede quedar vacio.");
        }
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'nombre' no puede ser null ni puede quedar vacio.");
        }
        if (edad <= 0) {
            throw new IllegalArgumentException("Invalido! El campo 'edad' debe ser mayor que 0.");
        } else {
            this.nacionalidad = nacionalidad;
            this.nombre = nombre;
            this.edad = edad;
        }
    }
// FUNCIONES
    public void pescar(Pez pezCapturado) throws Exception {
        if (pezCapturado == null) {
            throw new NullPointerException("Error: Pez no existe");
        } else {
        listaPecesCapturados.add(pezCapturado);
        System.out.println(
            this.nombre + " ha capturado al pez " + pezCapturado.getNombre()
            +
            "!!!\n\n"
            +
            pezCapturado.sonido()
            +
            "\n");
        }
    }
    
    public void mostrarPeces() throws Exception {
        if (listaPecesCapturados.size() == 0) {
            throw new Exception("Error: Lista de peces capturados vacia.");
        } else {
            for (Pez pez : this.listaPecesCapturados) {
                System.out.println(
                    "PECES CAPTURADOS POR '" + this.nombre + "'"
                    +
                    "\n"
                    +
                    "CAPTURA_1: " + pez.getNombre());
            }
        }
    }

// GETTERS & SETTERS
    public String getNacionalidad() {
        return this.nacionalidad;
    }
    public String getNombre() {
        return this.nombre;
    }
    public int getEdad() {
        return this.edad;
    }
    public String getTipo() {
        return "PESCADOR";
    }

    public List<Pez> getListaPecesCapturados() {
        return listaPecesCapturados;
    }    
    public void setNacionalidad(String nacionalidad) throws Exception {
        if (nacionalidad == null || nacionalidad.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'nacionalidad' no puede ser null ni estar vacio.");
        } else {
            this.nacionalidad = nacionalidad;
        }
    }
    public void setNombre(String nombre) throws Exception {
        if (nombre == null || nombre.isBlank()) {
            throw new IllegalArgumentException("Invalido! El campo 'nombre' no puede ser null ni estar vacio.");
        } else {
            this.nombre = nombre;
        }
    }
    public void setEdad(int edad) throws Exception {
        if (edad <= 0) {
            throw new IllegalArgumentException("Invalido! El campo 'edad' no puede ser null ni estar vacio.");
        } else {
            this.edad = edad;
        }
    }
}