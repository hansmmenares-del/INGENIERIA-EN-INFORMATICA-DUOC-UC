import java.util.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){

    int edad = 19;
    boolean estado = false;

    if(edad >= 18){
        estado = true;
    }else{
        estado = false;
    }
    
    System.out.println(estado);

    Scanner scanner = new Scanner(System.in);
    int opc = scanner.nextInt();
    scanner.close();

    switch (opc) {
        case 1:
            double saldo = 1000.0;
            double precio = 200.0;
            if (saldo >= precio){
                System.out.println("Compra exitosa");
            }else{
                System.out.println("Imposible hacer la compra");
            }
            break;
        case 2:
            if(precio > 40000.0){

            }else if(saldo < 0){
                System.out.println("hola");
            }
            break;
        case 3:
            break;
        default:
            break;
        
        }
    }
}