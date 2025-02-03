from turtle import Turtle

# Constant Terms

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0

        #Using data from data.txt
        with open("data.txt") as data:
            self.highscore = int(data.read()) 

        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("black")
        self.update_scoreboard()


    # Update Scoreboard after every point or high score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\t\t\tHigh score: {self.highscore}", align = ALIGNMENT ,font = FONT)


    # Setting and updating High score 
    def reset (self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open ("data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


    # Increase score after every point 
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()