"""
File: 
Name:Irene
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
size = 10
window=GWindow()
n=0 #次數預設值
start_x =0 #點擊 oval 的 x 初始值
start_y =0 #點擊 oval 的 y 初始值
oval = None #oval 初始值

def main():
    """
    This program creates line objects on a GWindow.
    A circle is displayed to indicate the user's first mouse click.
    When the user clicks on the canvas for the second time, the circle
    disappears and a line is drawn between the two clicked positions.
    """
    onmouseclicked(draw)


def draw(irene):
    global n, start_x, start_y, oval
    n+=1
    if n % 2 != 0:
        start_x=irene.x
        start_y=irene.y
        oval = GOval(size, size, x=irene.x-size/2, y = irene.y-size/2) #筆畫的左下角 - 球的直徑/2
        oval.filled = False
        oval.color = 'black'
        window.add(oval)
    else: #click > line > delete oval
        line = GLine(start_x, start_y, irene.x, irene.y)
        window.add(line)
        window.remove(oval) #oval 不在這裡，所以要用 gloval


if __name__ == "__main__":
    main()
