package frogger;
import javafx.fxml.FXML;
import javafx.scene.shape.Circle;

public class Frog extends Circle {
    int row = 0;


    public Frog() {
    }

    public void stepUp() {
        row++;
    }

    public void stepDown(){
        row--;
    }

}