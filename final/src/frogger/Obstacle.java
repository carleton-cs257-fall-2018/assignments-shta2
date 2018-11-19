package frogger;
import javafx.fxml.FXML;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Rectangle;

public class Obstacle extends Rectangle{
    private double velocityX;
    int row;

    public Obstacle(){};

    public Obstacle(double xPosition, int rowNum) {
        setX(xPosition);
        row = rowNum;
        setFill(Paint.valueOf("red"));
        setWidth(90);
        setHeight(40);
        setLayoutY((Controller.NUM_ROWS - rowNum) * Controller.ROW_WIDTH);
        velocityX = row * 5 + 5;
        if(row%2 == 0 ) {velocityX = -1 * velocityX;}
    }

    public void step() {
        this.setX(this.getX() + this.velocityX);
        if(getX() >= Controller.GAME_WIDTH  && velocityX > 0){
            setX(0 - getWidth());
        } else if (getX() + getWidth() <= 0 && velocityX < 0){
            setX(Controller.GAME_WIDTH );
        }
    }
}
