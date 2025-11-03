from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,260)
        self.color('white')
        with open('data.txt') as data:
            self.highscore = int(data.read())                      # Remember to write int
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')             # Need to write a string
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'     Game Over!\nYour final score is {self.score}', align=ALIGNMENT, font=FONT)
        
        
        