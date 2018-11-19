Paul Butterfield and Henry Pearson
Project Description: Our project is a frogger-esque game where the player will navigate a small "Frog" from the bottom of the screen to the top, 
all the while dodging horizontally scrolling obstacles of varying intervals and lengths. Upon reaching the top of the screen, the player scores a
certain amount of points, and then a new level is generated. If the player is hit by an obstacle, the game is over, and the player is returned to 
the start screen. 

Why we used MVC:
It makes sense for our project because we are creating a game where things have to be instantiated based on a set of rules, and 
can be changed based on that set of rules. 

Model Classes 

Frog() this is the player controlled sprite
Obstacles() this are the sidescrolling obstacles to be avoided

Views: 
Start Menu (start.fxml)
Game View   (game.fxml)

Controller:
Start Menu (Start.java)
Gameplay (Controller.java)

Models
Frog (Frog.javva)
Obstacles (Obstacle.java)

The graphics are quite simple but we believe all intended functionality is present.

