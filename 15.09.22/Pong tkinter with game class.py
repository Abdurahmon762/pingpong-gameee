# Written in OsX and IDLE

import tkinter
import time # and time.sleep(0.017) windows?

class Game():
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('pong game by abdurahmon')
        self.canvas = tkinter.Canvas(self.win, width=800,height=600, bg = 'black')
        self.canvas.pack()

    def new_game(self):
        self.player1_score = 0
        self.player2_score = 0
        
        
        self.paddle1 = self.canvas.create_rectangle(40, 255, 60, 345, fill = 'white')
        self.paddle2 = self.canvas.create_rectangle(740, 255, 760, 345, fill = 'white')
        self.ball = self.canvas.create_oval(400,300, 420, 320, fill = 'white')
        self.score = self.canvas.create_text(380, 50, fill = 'white', font= 'Courier 24 normal',
                                   text=(f' 0   0'))
        
        self.dx = 5
        self.dy = 5


        self.run()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            

    def events(self):
        self.canvas.bind_all('<KeyPress-w>', self.paddle_move)
        self.canvas.bind_all('<KeyPress-s>', self.paddle_move)
        self.canvas.bind_all('<KeyPress-Up>', self.paddle_move)
        self.canvas.bind_all('<KeyPress-Down>', self.paddle_move)
        
        

    def paddle_move(self, event):
        if event.keysym == 'w':
            self.canvas.move(self.paddle1, 0, -30)
        elif event.keysym == 's':
            self.canvas.move(self.paddle1, 0, 30)
        elif event.keysym == 'Up':
            self.canvas.move(self.paddle2, 0, -30)
        elif event.keysym == 'Down':
            self.canvas.move(self.paddle2, 0, 30)
            

    def update(self):
        time.sleep(0.017) # windows?
        
        # Move ball
        self.canvas.move(self.ball, self.dx, self.dy)

        # Position of ball
        self.ball_pos = self.canvas.coords(self.ball)
        self.paddle1_pos = self.canvas.coords(self.paddle1)
        self.paddle2_pos = self.canvas.coords(self.paddle2)
        # coords makes a list with 4 values[top left x,y, bottom right x,y]
        

        # Ball bounce at top/bottom
        if self.ball_pos[1] <= 0 or self.ball_pos[3] >= 600:
            self.dy *= -1
            

        # Paddle 1:
        if self.ball_pos[0] <= self.paddle1_pos[2] and self.ball_pos[0]>= self.paddle1_pos[0] and self.dx < 0:
            if self.ball_pos[3]>= self.paddle1_pos[1] and self.ball_pos[1]<= self.paddle1_pos[3]:
                self.dx *= -1

        # Paddle 2:
        elif self.ball_pos[2] >= self.paddle2_pos[0] and self.ball_pos[2]<= self.paddle2_pos[2] and self.dx > 0:
            if self.ball_pos[3]>= self.paddle2_pos[1] and self.ball_pos[1]<= self.paddle2_pos[3]:
                self.dx *= -1


        # Score player 1:
        if self.ball_pos[2]>=800:
            self.dx *= -1
            self.canvas.coords(self.ball, 400, 300, 420, 320)
            self.player1_score += 1
            self.canvas.delete(self.score)
            self.score = self.canvas.create_text(380, 50, fill = 'white', font= 'Courier 24 normal',
                                   text=(f' {self.player1_score}    {self.player2_score}'))

        # Score player 2:
        if self.ball_pos[0]<= 0:
            self.dx *= -1
            self.canvas.coords(self.ball, 400, 300, 420, 320)
            self.player2_score += 1
            self.canvas.delete(self.score)
            self.score = self.canvas.create_text(380, 50, fill = 'white', font= 'Courier 24 normal',
                                   text=(f' {self.player1_score}    {self.player2_score}'))
        
    
        self.win.update()

    def show_start_screen(self):
        self.waiting = True
        self.canvas.bind_all('<KeyPress-space>', self.wait_for_keypress)

        
        self.start_message = self.canvas.create_text(380, 250, fill = 'white', font= 'Courier 24 normal',
                                                 text=('pong game by abdurahmon\n\t Press "space" to start'))
            
        self.win.update()
        
        while self.waiting:
            self.win.update()

        self.canvas.delete(self.start_message)

    def show_game_over_screen(self):
        pass
            
      

    def wait_for_keypress(self, event):
        if event.keysym == 'space':
            self.waiting = False



game = Game()
game.show_start_screen()

while True:
    game.new_game()
    game.show_game_over_screen()
        
        
