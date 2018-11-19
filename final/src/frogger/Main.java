/*
Paul Butterfield and Henry Pearson

Launches JavaFX application to play "Frogger!"
 */
package frogger;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

public class Main extends Application {


    @Override
    public void start(Stage primaryStage) throws Exception{
        primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            @Override
            public void handle(WindowEvent t) {
                Platform.exit();
                System.exit(0);
            }
        });

        FXMLLoader startLoader = new FXMLLoader(getClass().getResource("start.fxml"));
        Parent startRoot = (Parent)startLoader.load();
        primaryStage.setTitle("Frogger");
        Scene startScene = new Scene(startRoot, 1000, 500);
        primaryStage.setScene(startScene);
        primaryStage.show();
        startRoot.requestFocus();

    }


    public static void main(String[] args) {
        launch(args);
    }

}
