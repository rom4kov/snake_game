from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.speed("fastest")
        snake_part.goto(position)
        self.body.append(snake_part)

    def move(self):
        for part_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part_num - 1].xcor()
            new_y = self.body[part_num - 1].ycor()
            self.body[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        tail_pos = self.body[-1].pos()
        self.add_part(tail_pos)

    def reset(self):
        for part in self.body:
            part.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
