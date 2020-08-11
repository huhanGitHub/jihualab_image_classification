from PIL import Image

print(__file__)

im = Image.open('D:\projects\pytorch_classification-master\pytorch_classification-master\data\sample\EM-F-1224.png')
im.show()
im_rotate1 = im.rotate(45)
im_rotate2 = im.transpose(Image.FLIP_LEFT_RIGHT)
im_rotate3 = im.transpose(Image.FLIP_TOP_BOTTOM)
im_rotate4 = im.transpose(Image.ROTATE_90)
im_rotate5 = im.transpose(Image.ROTATE_180)
im_rotate6 = im.transpose(Image.ROTATE_270)

im_rotate1.show()
im_rotate2.show()
im_rotate3.show()
im_rotate4.show()
im_rotate5.show()
im_rotate6.show()

im_rotate2.save('D:\projects\pytorch_classification-master\pytorch_classification-master\data\sample\EM-F-1224_1.png')