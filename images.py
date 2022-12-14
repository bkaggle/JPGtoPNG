from PIL import Image, ImageFilter

img=Image.open('./image/4.3 pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
converted_img=img.convert('L')
converted_img.save('grey.png','png')
filtered_img.save('blur_pikachu.png', 'png')
resize=converted_img.resize((300,300))
box=(100, 100, 400, 400)
croped = converted_img.crop(box)
croped.save('pikachu_crop.png', 'png')
resize.show()
converted_img.show()
print(img)

print('the format is ', img.format)
print('image size is ', img.size)
print('image mode is ', img.mode)