"""
File: fire.py
Name: Irene
---------------------------------
This file contains a function called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""


from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05 #大火 pixel

def main():
    """
    :param filename: original_fire
    :return: image with highlight fire place, and other places are gray-scale
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png') #function
    highlighted_fire.show()


def highlight_fires(filename): #def function
    """
    :param filename: original_fire
    :return: image with highlight fire place, and other places are gray-scale
    """
    img = SimpleImage(filename) #圖像路徑打開/從執行檔開始算
    for pixel in img: #在 img 找每一個像素
        avg = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else: #非 pixel.red > avg*HF 的地方呈現灰階
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
