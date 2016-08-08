__author__ = 'Paul'
from PIL import Image
from PIL import ImageFilter

class ConvertImages():

    def open_image(self, picture):
         return Image.open(picture)

    def convert_to_black_white(self, image):
        return image.convert("L")

    def blur_image(self, image):
        return image.filter(ImageFilter.BLUR)

    def detail_of_image(self, image):
        return image.filter(ImageFilter.DETAIL)

    def find_edges_of_image(self, image):
        return image.filter(ImageFilter.FIND_EDGES)


x = ConvertImages()
picture = x.open_image("piggie.jpg")
black_white_picture = x.convert_to_black_white(picture)
black_white_picture.show()

blur_picture = x.blur_image(picture)
blur_picture.show()

detailled_picture = x.detail_of_image(picture)
detailled_picture.show()

edges_picture = x.find_edges_of_image(picture)
edges_picture.show()