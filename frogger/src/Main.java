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

        FXMLLoader loader = new FXMLLoader(getClass().getResource("pong.fxml"));
        Parent root = (Parent)loader.load();
        Controller controller = loader.getController();


        primaryStage.setTitle("Kinda Pong");
        Scene scene = new Scene(root, 700, 500);
        primaryStage.setScene(scene);
        scene.setOnKeyPressed(controller);
        primaryStage.show();

        // Solution: once the Stage is displayed, explicitly put the focus on the root node.
        // You could, alternatively, go to Controller.initialize and do this.paddle.requestFocus().
        root.requestFocus();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
