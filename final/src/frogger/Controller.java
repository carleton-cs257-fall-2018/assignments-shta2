package frogger;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Shape;
import javafx.scene.layout.Region;

import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

public class Controller implements EventHandler<KeyEvent> {
    final static int NUM_ROWS = 7;
    final static int ROW_WIDTH = 40;
    final private double FRAMES_PER_SECOND = 20.0;
    final static double GAME_WIDTH = 1000;

    @FXML private AnchorPane gameBoard;
    @FXML private Frog frog;



    private boolean lost = false;
    private Timer timer;
    private ArrayList<Obstacle> obstacleList = new ArrayList<>();

    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();
        double frogPosition = frog.getLayoutX();
        double stepSize = 15.0;
        if (code == KeyCode.LEFT) {
            // move frog left
            if (frogPosition - frog.getRadius() > stepSize) {
                this.frog.setLayoutX(this.frog.getLayoutX() - stepSize);
            } else {
                this.frog.setLayoutX(frog.getRadius());
            }
            keyEvent.consume();
        } else if (code == KeyCode.RIGHT ) {
            // move frog right
            //double radius = frog.getRadius();
            //double width = this.gameBoard.getWidth();
            if (frogPosition + frog.getRadius() + stepSize < GAME_WIDTH) {
                this.frog.setLayoutX(this.frog.getLayoutX() + stepSize);
            } else {
                this.frog.setLayoutX(GAME_WIDTH - this.frog.getRadius());
            }
            keyEvent.consume();
        }  else if (code == KeyCode.UP ) {
            frog.stepUp();
        } else if (code == KeyCode.DOWN && frog.row != 0){
            frog.stepDown();
        }
    }

    public void initialize() {
        this.startTimer();
    }

    public void setInitialObjects(){
        frog.row = 0;
        for (int i = 1; i < NUM_ROWS; i++){
            Obstacle newObstacle = new Obstacle(100 * i, i);
            obstacleList.add(newObstacle);
            gameBoard.getChildren().add(newObstacle);
        }
    }

    private void startTimer() {
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                Platform.runLater(new Runnable() {
                    public void run() {
                        updateAnimation();
                    }
                });
            }
        };

        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }

    private void updateAnimation() {
        frog.setLayoutY((NUM_ROWS - frog.row) * ROW_WIDTH + frog.getRadius());
        for (Obstacle obstacle : obstacleList){
            obstacle.step();
            if (obstacle.row == frog.row && frog.getLayoutX() - frog.getRadius() - obstacle.getWidth() < obstacle.getX() && obstacle.getX() < frog.getLayoutX() + frog.getRadius()){
                lost = true;
            }
        }


    }
}
