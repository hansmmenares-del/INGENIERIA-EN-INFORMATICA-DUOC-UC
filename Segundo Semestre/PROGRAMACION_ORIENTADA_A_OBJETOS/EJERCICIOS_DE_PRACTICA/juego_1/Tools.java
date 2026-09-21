import java.util.InputMismatchException;
import java.util.Scanner;

public class Tools{
    
    static Scanner scanner = new Scanner(System.in);
    
    public int selectOption(int lowLim, int upperLim, String msg) {
        
        int opc = 0; 

        while (true) {
            try {

                opc = scanner.nextInt();
                if (opc >= lowLim && opc <= upperLim) {
                    return opc;
                }
            }
            catch(InputMismatchException e) {
                System.out.println("Invalid!");
                scanner.nextLine();
            }
        }        
    }
    public String stringInput() {
        return scanner.next();
    }
    public double doubleInput() {
        return scanner.nextDouble();
    }

}