import characters.Character;
import gamewindow.GamePanel;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main {
    public static void main(String[] args) {
        
        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(false);
        window.setTitle("_- HOLA -_");
        GamePanel gamePanel = new GamePanel();
        window.add(gamePanel);
        window.pack();
        window.setLocationRelativeTo(null);
        window.setVisible(true);
        
        gamePanel.startGameThread();


        Tools tool = new Tools();
        System.out.println(
            "\n"
            +
            "========================================"
            +
            "\n"
            +
            "LAS RUINAS DE ELDORIA"
            +
            "\n"
            +
            "========================================"
            +
            "\n"
            +
            "1. Crear personaje"
            +
            "\n"
            +
            "2. Salir Seleccione una opción: "
            +
            "\n"
        );
        
        int opc = tool.selectOption(1, 2, "Hola");
        
        if (opc == 1) {
            
            Character mainCharacter = new Character(tool.stringInput(), 5, 100, 1, 2, 1, 1);
        }
    }
}