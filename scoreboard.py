from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def add_score_point(self):
        self.score += 1
        self.write_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.write_score()
        self.print_game_over()

    def print_press_space(self):
        self.goto(0, -290)
        self.color("white")
        self.write("Press SPACE to start", False, align=ALIGNMENT, font=FONT)
