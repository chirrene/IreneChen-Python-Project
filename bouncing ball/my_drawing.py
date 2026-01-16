"""
File: 
Name:Irene
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This is my lovely pet : Cute and Fat Beagle!!!
    """
    window = GWindow(width=800, height=500, title="MyBeagle")  # 創建畫布
    face = GOval(280, 250, x= (window.width-280)/2, y=(window.height-250)/2)
    face.filled = True
    face.fill_color='tan'
    face.color = 'tan'
    window.add(face)

    face2 = GOval(140, 100, x= (window.width-140)/2, y=250)
    face2.filled = True
    face2.fill_color = 'white'
    face2.color = 'white'
    window.add(face2)

    eye_l = GOval(55, 50, x=320, y=180)
    eye_l.filled = True
    eye_l.fill_color = 'black'
    eye_l.color = 'black'
    window.add(eye_l)

    eye_r = GOval(55, 50, x=430, y=180)
    eye_r.filled = True
    eye_r.fill_color = 'black'
    eye_r.color = 'black'
    window.add(eye_r)

    eye_in_l = GOval(10, 10, x=330, y=200)
    eye_in_l.filled = True
    eye_in_l.fill_color = 'white'
    eye_in_l.color = 'white'
    window.add(eye_in_l)

    eye_in_r = GOval(10, 10, x=440, y=200)
    eye_in_r.filled = True
    eye_in_r.fill_color = 'white'
    eye_in_r.color = 'white'
    window.add(eye_in_r)

    nose = GOval(70, 50, x= (window.width-70)/2, y=280)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'black'
    window.add(nose)

    rect = GRect(25, 150, x= (window.width-20)/2, y=120)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    window.add(rect)

    ear_l = GOval(50, 180)
    ear_l.filled = True
    ear_l.fill_color = 'saddlebrown'
    ear_l.color = 'saddlebrown'
    window.add(ear_l)

    ear_l.x = 250  # 左上角 x
    ear_l.y = 170  # 左上角 y

    ear_r = GOval(50, 180)
    ear_r.filled = True
    ear_r.fill_color = 'saddlebrown'
    ear_r.color = 'saddlebrown'
    window.add(ear_r)

    ear_r.x = 500  # 左上角 x
    ear_r.y = 170  # 左上角 y

    ear_l2 = GOval(80, 140)
    ear_l2.filled = True
    ear_l2.fill_color = 'saddlebrown'
    ear_l2.color = 'saddlebrown'
    window.add(ear_l2)

    ear_l2.x = 220  # 左上角 x
    ear_l2.y = 230  # 左上角 y

    ear_r2 = GOval(80, 140)
    ear_r2.filled = True
    ear_r2.fill_color = 'saddlebrown'
    ear_r2.color = 'saddlebrown'
    window.add(ear_r2)

    ear_r2.x = 500  # 左上角 x
    ear_r2.y = 230  # 左上角 y

    label = GLabel("BEAGLE")
    label.font = '-180'
    label.color = 'GREY'
    window.add (label, x= 75, y=label.height) #字體高

if __name__ == '__main__':
    main()
