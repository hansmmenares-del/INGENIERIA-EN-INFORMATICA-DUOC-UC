package characters;

public class Character{
    String name;
    double attack;
    double hp;
    double exp;
    double charisma;
    double stamina;
    double intelligence;

    public Character(
        String name,
        double attack, 
        double hp,
        double exp, 
        double charisma,
        double stamina,
        double intelligence) {
            this.name = name;
            this.attack = attack;
            this.hp = hp;
            this.exp = exp;
            this.charisma = charisma;
            this.stamina = stamina;
            this.intelligence = intelligence;
    }


}