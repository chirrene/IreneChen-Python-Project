"""
File: mirror_lake.py
Name:Irene
----------------------------------
This program reads the image “mt-rainier.jpg” and generates a 
new image that creates a mirror-lake effect by placing an 
inverted copy of the original image beneath it.
"""


from simpleimage import SimpleImage


def main():
    """
    :param filename:original_mt
    :return: vertically reflected orginal_my
    """
    original_img = SimpleImage('images/mt-rainier.jpg') #讀圖片檔
    original_img.show()
    reflected_img = reflect('images/mt-rainier.jpg') #讀圖片檔
    reflected_img.show()

def reflect(filename):
    """
    :param filename:original_mt
    :return: vertically reflected orginal_my
    """
    img= SimpleImage(filename) #圖像路徑打開
    b_img = SimpleImage.blank (img.width*1, img.height*2) #製作空白畫布
    for y in range (img.height):
        for x in range (img.width):
            imgp=img.get_pixel(x,y) #去原圖片 img 裡面，拿出座標 (x, y) 的 pixel
            bp_up = b_img.get_pixel(x,y)
            bp_up.red = imgp.red
            bp_up.green = imgp.green
            bp_up.blue = imgp.blue
            bp_down = b_img.get_pixel(x,b_img.height-1-y)
            bp_down.red = imgp.red
            bp_down.green = imgp.green
            bp_down.blue = imgp.blue
    return b_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
