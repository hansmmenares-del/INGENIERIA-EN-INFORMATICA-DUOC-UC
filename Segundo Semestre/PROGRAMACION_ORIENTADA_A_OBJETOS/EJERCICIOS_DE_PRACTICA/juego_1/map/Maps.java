package map;
import characters.*;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.JLabel;

public class Maps {
    List<List<Integer>> territory = new ArrayList<>();

    public Maps(List<List<Integer>> territory) {
        this.territory = territory;
    }

    void entitisInMap(List<List<Integer>> territory){
        for (List<Integer> i : territory) {
            int texture = i.get(0);
            int enemy = i.get(1);
            int velocity = i.get(2);

        }
    }

    public void texture(int texture_enemmy_velocity) {

        switch (texture_enemmy_velocity) {
            case 0:
                //frame.add(new JLabel(new ImageIcon("Path/To/Your/Image.png")));
            case 1:
                break;
            case 2:
                break;
            default:
                break;
        }
    }

}