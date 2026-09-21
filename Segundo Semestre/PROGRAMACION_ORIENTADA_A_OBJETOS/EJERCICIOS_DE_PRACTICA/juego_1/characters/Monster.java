package characters;

import java.util.List;

public class Monster extends Character {

    double poison;

    public Monster(
        String name,
        double attack,
        double hp,
        double exp,
        double charisma,
        double stamina,
        double intelligence) {

        super(name, attack, hp, exp, charisma, stamina, intelligence);
        this.poison = poison;
        
    }
}