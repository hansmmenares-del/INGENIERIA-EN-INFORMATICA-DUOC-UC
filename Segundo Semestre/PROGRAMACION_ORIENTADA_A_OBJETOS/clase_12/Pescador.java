import java.util.List;

public class Pescador{

    private List<Pez> listaPescados;
    private String nombre;
    private int edad;
    private String nacionalidad;

    public Pescador(
        String nombre,
        int edad,
        String nacionalidad) {

            this.nombre = nombre;
            this.edad = edad;
            this.nacionalidad = nacionalidad;        
        }

    public void pescarPez(Pez pez, Pescador pescador) {
        listaPescados.add(pez);
        System.out.println(
                getNombre(pescador)
                        +
                        " ha pescado un "
                        +
                        pez.getNombre(pez)
        );
    }
    public void mostrarPeces(){
        for (Pez pezEnLista : getListaPescados()) {

            System.out.println(
                "NOMBRE DEL PEZ: "
                +
                pezEnLista.getNombre(pezEnLista)
                +
                "\n"
                +
                "PESO DEL PEZ (Kg): "
                +
                pezEnLista.getPeso(pezEnLista)
                +
                "\n"
                +
                "LONGITUD DE PEZ: "
                +
                pezEnLista.getLongitud(pezEnLista)

            );
        }
    }

    public String getNombre(Pescador pescador) {
        return this.nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getEdad(Pescador pescador) {
        return this.edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public String getNacionalidad(Pescador pescador) {
        return this.nacionalidad;
    }
    public void setNacionalidad(String nacionalidad) {
        this.nacionalidad = nacionalidad;
    }
    public List<Pez> getListaPescados() {
        return listaPescados;
    }
    public void setListaPescados(List<Pez> listaPescados) {
        this.listaPescados = listaPescados;
    }
}