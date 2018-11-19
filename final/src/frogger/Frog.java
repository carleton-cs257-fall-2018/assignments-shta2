/*
Paul Butterfield and Henry Pearson
Model of Frog
 */
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