/*
Paul Butterfield and Henry Pearson
The start menu contains simple score information as well as a button to launch the game.
 */
package frogger;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;


public class Start {
    @FXML private Button startButton;
    @FXML private Button resetButton;
    @FXML private Label scoreLabel;
    @FXML private Label highScoreLabel;



    public void initialize() {
        startButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent e) {
                Controller.score = 0;
                Parent root = null;
                Controller controller = null;
                try {
                    FXMLLoader loader = new FXMLLoader(getClass().getResource("game.fxml"));
                    root = (Parent) loader.load();
                    controller = loader.getController();
                    //
                } catch (Exception except) {

                }
                if (root != null && controller != null) {
                    Scene scene = new Scene(root, 1000, 500);
                    Stage stage = (Stage) startButton.getScene().getWindow();
                    stage.setScene(scene);
                    scene.setOnKeyPressed(controller);
                    controller.setInitialObjects();
                }
            }
        });

        scoreLabel.setText("Your Score: " + Controller.score);
        highScoreLabel.setText("Your Previous Best: " + Controller.highScore);

        resetButton.setOnAction(new EventHandler<ActionEvent>(){
            @Override
            public void handle(ActionEvent e){
                Controller.highScore = 0;
                highScoreLabel.setText("Your Previous Best: 0");
            }
        });

    }
}
