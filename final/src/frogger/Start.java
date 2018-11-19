package frogger;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.*;



public class Start {
    @FXML private Button startButton;
    @FXML private Button resetButton;


    startButton.setOnAction(new EventHandler<ActionEvent>() {
        @Override public void handle() {
            int a =2;
        }
    });

}
