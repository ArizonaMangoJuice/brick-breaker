from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.graphics import Color

# class for making a brick in the game
class Brick(Widget):
    # creates hit detection for when the ball hits the brick
    def hitBrick(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            print(self.x)
            self.x = -150
            
# class for making the paddle in the game
class Paddle(Widget):
    # creates hit detection for when the ball hits the paddle
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * -8.574355240000006, 0.48346681823204063)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


# class for creating the ball in the game
class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # method to move the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# class for creating the Game
class Game(Widget):
    # create the ball player and the bricks
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    brick1 = ObjectProperty(None)
    brick2 = ObjectProperty(None)
    brick3 = ObjectProperty(None)
    brick4 = ObjectProperty(None)
    brick5 = ObjectProperty(None)
    brick6 = ObjectProperty(None)
    brick7 = ObjectProperty(None)
    brick8 = ObjectProperty(None)
    brick9 = ObjectProperty(None)
    brick10 = ObjectProperty(None)
    test = Button(text='')

    # When the class get called start method will run first
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.start()
        
    # hides the gameOver button when the player clicks restart
    def hideRestart(self):
        self.start()
        self.test.x = -500

    # starts the clock to let the game run
    def start(self):
        Clock.unschedule(self.update)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    # stops the clock to pause the game
    def stop(self):
        Clock.unschedule(self.update)    

    # resets all bricks back to original spot
    def reset(self):
        self.brick1.x = self.width - 35
        self.brick2.x = self.width - 35
        self.brick3.x = self.width - 35
        self.brick4.x = self.width - 85
        self.brick5.x = self.width - 85
        self.brick6.x = self.width - 85
        self.brick7.x = self.width - 135
        self.brick8.x = self.width - 135
        self.brick9.x = self.width - 135
        self.brick10.x = self.width - 185

    # method for the ball speed and placement
    def serve_ball(self, vel=(-8.574355240000006, 0.48346681823204063)):
        self.ball.center = [104.0, 300]
        self.ball.velocity = vel

    # main method that runs when the clock starts
    def update(self, dt):
        # start the ball 
        self.ball.move()
        # initialize the method for the paddle
        self.player1.bounce_ball(self.ball)
        # initialize the method for the bricks
        self.brick1.hitBrick(self.ball)
        self.brick2.hitBrick(self.ball)
        self.brick3.hitBrick(self.ball)
        self.brick4.hitBrick(self.ball)
        self.brick5.hitBrick(self.ball)
        self.brick6.hitBrick(self.ball)
        self.brick7.hitBrick(self.ball)
        self.brick8.hitBrick(self.ball)
        self.brick9.hitBrick(self.ball)
        self.brick10.hitBrick(self.ball)
        # if all the bricks are hit
        if (
            self.brick10.x == -150 and 
            self.brick9.x == -150 and 
            self.brick8.x == -150 and
            self.brick7.x == -150 and
            self.brick6.x == -150 and
            self.brick5.x == -150 and
            self.brick4.x == -150 and
            self.brick3.x == -150 and
            self.brick2.x == -150 and
            self.brick1.x == -150
           ):
            self.stop()
            self.serve_ball(vel=(4, 0))
            self.reset()
            self.test.center_x = self.parent.height / 2
            self.test.center_y = self.parent.height / 2
        
        # if the ball hits the top or bottom of the screen bounce the ball
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # if the ball hits the right side of the screen bounce
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        # if the ball hits the left side of the screen reset
        if self.ball.x < self.x:
            self.serve_ball(vel=(4, 0))
            print(self.brick1.x)
            self.reset()

    # allows you to move the paddle by clicking it
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y

# class that lets you have screens for the app
class Manager(ScreenManager):
    pass

# root Widget 
class ScreensApp(App):
    # build methods get detected by kivy and runs first
    def build(self):
        # load the kivy file
        self.load_kv('brickBreaker.kv')
        # when the user clicks the button doa WipeTransition
        return Manager(transition=WipeTransition())

if __name__ == '__main__':
    ScreensApp().run()