from PIL import Image
import glob

image_list = []
for filename in glob.glob('input/*.jpg'):  # image format must be jpg
    single_image = Image.open(filename)
    final_img = single_image.convert('RGB')
    image_list.append(final_img)


# print(image_list[1])
if len(image_list) == 0:
    print("No image found! Try again!")
else:
    image_list[0].save(r'output\my_pdf.pdf', save_all=True, append_images=image_list[1:])