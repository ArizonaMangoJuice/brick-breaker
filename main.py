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
class Brick(Widget):
    def hitBrick(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            print(self.x)
            self.x = -150
            

class Paddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            # vx, vy = [-8.574355240000006, 0.48346681823204063]
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * -8.574355240000006, 0.48346681823204063)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            self.score += 1

class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    brick1 = ObjectProperty(None)
    # brick1.Color(1, 1, 1, 1)
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
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        # self.test.bind(on_release = self.serve_ball(vel=(4, 0))
        self.start()
        

    def hideRestart(self):
        self.start()
        self.test.x = -500

    def start(self):
        Clock.unschedule(self.update)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def stop(self):
        # Stop updating
        Clock.unschedule(self.update)    

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

    def serve_ball(self, vel=(-8.574355240000006, 0.48346681823204063)):
        self.ball.center = [104.0, 300]
        print(vel)
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
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
           
            # self.test.text = 'game Over'
            print(self.parent.height)
            self.test.center_x = self.parent.height / 2
            self.test.center_y = self.parent.height / 2
            # self.test.on_release =  self.serve_ball(vel=(4, 0))
            print('test x',self.test.center)
            
            # self.start()
        
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        if self.ball.x < self.x:
            self.serve_ball(vel=(4, 0))
            print(self.brick1.x)
            self.reset()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y


class Manager(ScreenManager):
    pass

class ScreensApp(App):
    def build(self):
        root = self.root
        self.load_kv('brickBreaker.kv')
        return Manager(transition=WipeTransition())

if __name__ == '__main__':
    ScreensApp().run()