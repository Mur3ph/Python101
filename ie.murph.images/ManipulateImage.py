__author__ = 'Paul'
from PIL import Image
class ManipulateImages():

    def open_image(self, picture):
         return Image.open(picture)

    def resize_image(self, image):
        return image.resize((250, 250))

    def flip_picture(self, image):
        return image.transpose(Image.FLIP_LEFT_RIGHT)

    def spin_image(self, image):
        return image.transpose(Image.ROTATE_90)


x = ManipulateImages()
image = x.open_image("piggie.jpg")
resized_image = x.resize_image(image)
flipped_image = x.flip_picture(image)
spun_image = x.spin_image(image)

resized_image.show()
flipped_image.show()
spun_image.show()



