"""
File: bouncing_ball.py
Name:Irene
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 0 #初始化垂直速度
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball_falling = False #use boolen to control the stimulation of ball falling
out_falling_number = 0 #右牆掉出去次數的初始值

# design oval
oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
oval.filled = True
oval.fill_color = 'black'
window.add(oval)


def main():
    """
    This program simulates a bouncing ball that starts at
    the position (START_X, START_Y).
    The ball moves with an initial x velocity VX and an
    initial y velocity of 0. Each time the ball bounces,
    its y velocity is reduced by a factor defined as REDUCE.
    """
    onmouseclicked(ball_fall)


def ball_fall(event): #function 傳 function
    """
    This program define the function of ball_fall
    when ball is falling, clicking the window cannot stimulate a bouncing ball
    However, if the ball is not falling, the clicking the window will stimulate a bouncing ball.
    When you click the window, the ball will start to drop
    """
    #初始化，球要點擊才會出現並往下掉
    global ball_falling
    if not ball_falling: #沒有在 falling 的時候開關才會打開
        ball_falling = True
        ball_drop()


def ball_drop():
    """
    This program define the function of ball_drop
    when ball is falling, the ball vertical velocity = VX, and the horizontal velocity = VY
    If the oval touch the bottom, the oval will rebound
    The vertical velocity may increase when the number of falling increase.
    """
    global oval, VY
    while ball_falling:
        VY += GRAVITY
        oval.move(VX,VY)
        if oval.y + oval.height >= window.height:
            VY = -VY
        ball_return()
        pause(DELAY)


def ball_return():
    """
    Once the ball touches the far right edge, and the number of out_falling is more than three times,
    the ball will stop falling, and move to the initial position.
    """
    global oval, out_falling_number, VY, ball_falling
    if oval.x + SIZE > window.width:
        out_falling_number += 1
        if out_falling_number > 3:
            ball_falling = False
            oval.x = START_X
            oval.y = START_Y
            VY=0
            pause(DELAY)


if __name__ == "__main__":
    main()
