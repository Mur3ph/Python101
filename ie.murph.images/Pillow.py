__author__ = 'Paul'
from PIL import Image

class UsingPillow(object):

    def open_image(self, picture):
        return Image.open(picture)

    def size_of_image(self, picture):
        print(picture.size)

    def format_of_image(self, picture):
        print(picture.format)

    def show_image(self, picture):
        picture.show()

    def crop_image(self, picture, over_one, down_one, over_two, down_two):
        test_area = (100, 100, 300, 375) #100 over and 100 down, 300 over and 375 down
        area = (over_one, down_one, over_two, down_two)
        return picture.crop(area)


#TUTORIAL 43 - Cropping an image
x = UsingPillow()
image = x.open_image("spudy.jpg")
x.show_image(image)
cropped_image_1 = x.crop_image(image, 100, 100, 300, 375)
x.show_image(cropped_image_1)

#TUTORIAL 44 - Cropping and Putting two images together
image_1 = x.open_image("spudy.jpg")
image_2 = x.open_image("me.jpg")
image_3 = x.open_image("ismise.jpg")

area = (160, 220, 300, 375)
area_to_crop = (100,200,300,200)

cropped_image_2 = x.crop_image(image_3, *area)
#cropped_image_3 = x.crop_image(image_2, *area_to_crop)

image_1.paste(cropped_image_2, area)
x.show_image(image_1)
#x.show_image(cropped_image_2)
#x.show_image(cropped_image_3)

# x.size_of_image(image_3)






