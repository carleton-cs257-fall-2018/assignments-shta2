package frogger;

import javafx.fxml.FXML;
import javafx.scene.shape.Circle;

public class Frog extends Circle {
    int row = 0;


    public Frog() {
        setCenterX(300);
        setCenterY(Controller.NUM_ROWS * Controller.ROW_WIDTH);
    }

    public void stepUp() {
        row++;
    }

    public void stepDown(){
        row--;
    }

}