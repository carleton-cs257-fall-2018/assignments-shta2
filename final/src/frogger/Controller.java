package frogger;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.TimeUnit;


/*
Controls the movement of the frog and the obstacles during gameplay and
determines when the player has moved to a next level or lost the game.
 */
public class Controller implements EventHandler<KeyEvent> {
    final static int NUM_ROWS = 7;
    final static int ROW_WIDTH = 40;
    final private double FRAMES_PER_SECOND = 20.0;
    final static double GAME_WIDTH = 1000;

    @FXML private AnchorPane gameBoard;
    @FXML private Frog frog;
    @FXML private Label gameOver;


    private boolean lost = false;
    static int score = 0;
    static int highScore = 0;
    private Timer timer;
    private ArrayList<Obstacle> obstacleList = new ArrayList<>();


    /*
    Moves the frog in response to the player's input as long as the game is not over.

    @Param KeyEvent keyEvent
     */
    @Override
    public void handle(KeyEvent keyEvent) {
        if(lost){
            return;
        }
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
            if (frogPosition + frog.getRadius() + stepSize < GAME_WIDTH) {
                this.frog.setLayoutX(this.frog.getLayoutX() + stepSize);
            } else {
                this.frog.setLayoutX(GAME_WIDTH - this.frog.getRadius());
            }
            keyEvent.consume();
        }  else if (code == KeyCode.UP ) {
            //move frog up
            frog.stepUp();
        } else if (code == KeyCode.DOWN && frog.row != 0){
            //move frog down
            frog.stepDown();
        }
    }

    public void initialize() {
        this.startTimer();
    }

    /*
    Creates the frog and all the obstacles on screen.
     */
    public void setInitialObjects(){
        frog.row = 0;
        frog.setLayoutX(500);
        for (int i = 1; i < NUM_ROWS; i++){
            Obstacle newObstacle = new Obstacle(100 * i, i);
            obstacleList.add(newObstacle);
            gameBoard.getChildren().add(newObstacle);
        }
    }

    /*
    Increases the score and the difficulty every time the player beats a level.
     */
    private void nextLevel(){
        for (Obstacle obstacle : obstacleList){
            obstacle.setVelocityX(obstacle.getVelocityX() * 1.15);
        }
        frog.row = 0;
        score++;
    }

    /*
    Displays the 'Game Over' message, then returns to the start menu.
     */
    private void endGame(){
        try {
            TimeUnit.MILLISECONDS.sleep(300);
        } catch (Exception except) {}

        Parent root = null;
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("start.fxml"));
            root = (Parent) loader.load();
        } catch (Exception except) {}

        if (root != null && gameOver.getScene().getWindow() != null) {
            Scene scene = new Scene(root, 1000, 500);
            Stage stage = (Stage) gameOver.getScene().getWindow();
            stage.setScene(scene);
        }

        //update the high score
        if(score > highScore){
            highScore = score;
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
        //if the player reaches the top of the screen, they won the level
        if(frog.row >= NUM_ROWS){
            nextLevel();
        } else if(lost) {
            endGame();
            timer.cancel();
        }
        for (Obstacle obstacle : obstacleList){
            obstacle.step();
            //if the player overlaps with any of the obstacles, they've lost
            if (obstacle.row == frog.row && frog.getLayoutX() - frog.getRadius() - obstacle.getWidth() < obstacle.getX() && obstacle.getX() < frog.getLayoutX() + frog.getRadius()) {
                lost = true;
                gameOver.setStyle("-fx-opacity:100; -fx-font-size: 20");
            }
        }
    }
}
