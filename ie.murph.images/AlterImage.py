__author__ = 'Paul'

from PIL import Image

class UsingPillow():

     def open_image(self, picture):
        return Image.open(picture)


#TUTORIAL 45 - Changing colours to an image
x = UsingPillow()

#Images are made up into three colours and we are going to break up each of these into three variables
image_1 = x.open_image("mise_.jpg")
#print(image_1.mode)
red1, blue1, green1 = image_1.split()

#red1.show()
#blue1.show()
#green1.show()


#TUTORIAL 46 - Merging Image colours
image_2 = x.open_image("spudy.jpg")
red2, blue2, green2 = image_2.split()

colours1 = (red1, green1, blue1)
colours2 = (red2, green1, blue2)

new_image1 = Image.merge("RGB", colours1)
new_image2 = Image.merge("RGB", colours2)

#Crashing because images are different sizes but works none the less :)
new_image1.show()
new_image2.show()


