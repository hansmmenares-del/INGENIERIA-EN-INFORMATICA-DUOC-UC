package characters;
public class Hero extends Character{

    String weapon;

    public Hero(String name, int attack, int hp, int exp, int charisma, int stamina, int intelligence, String weapon) {
        super(name, attack, hp, exp, charisma, stamina, intelligence);
        this.weapon = weapon; 
    }
}