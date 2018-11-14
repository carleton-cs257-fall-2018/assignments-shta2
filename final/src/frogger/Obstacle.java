package frogger;
import javafx.fxml.FXML;
import javafx.scene.shape.Rectangle;

public class Obstacle extends Rectangle{
    private double velocityX;
    private double velocityY;

    public Obstacle() {
    }

    public void step() {
        this.setX(this.getX() + this.velocityX);
        this.setY(this.getY() + this.velocityY);
    }
}
