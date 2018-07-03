from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

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
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

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
    brick2 = ObjectProperty(None)
    brick3 = ObjectProperty(None)
    brick4 = ObjectProperty(None)
    brick5 = ObjectProperty(None)
    brick6 = ObjectProperty(None)
    # player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        # print(self.ball.center)
        self.ball.center = [104.0, 300]
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
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
        # self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            # self.player2.score += 1
            self.serve_ball(vel=(4, 0))
            print(self.brick1.x)
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
        # if self.ball.x > self.width:
        #     self.player1.score += 1
        #     self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        # if touch.x > self.width - self.width / 3:
            # self.player2.center_y = touch.y


class brickBreaker(App):
    def build(self):
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    brickBreaker().run()