from PIL import Image, ImageDraw, ImageFont, ImageOps
import matplotlib.pyplot as plt
import random

colours = [
    "#ec3750", '#ff8c37', '#f1c40f', '#33d6a6', '#5bc0de', '#338eda',
    '#a633d6', '#8492a6'
]
width, height = 1000, 1000


def draw_logo(letter):
    img = Image.linear_gradient('L').resize(
        (1000, 1000)).rotate(random.randrange(0, 90))

    img = img.crop(((img.width - width) / 2, (img.height - height) / 2,
                    (img.width + width) / 2, (img.height + height) / 2))

    choices = []
    for i in range(2):
        choices.append(random.choice(colours))
        colours.remove(choices[-1])
    choices = sorted(choices)

    img = ImageOps.colorize(img, black=choices[0], white=choices[1])

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Bold.ttf', size=500)
    draw.text((250, 250), letter, fill='white', font=font, anchor='mm')

    return img


img = Image.new('RGB', (1000, 1000))

img1 = draw_logo('h')
img.paste(img1, (0, 0))
img2 = draw_logo('a')
img.paste(img2, (500, 0))
img3 = draw_logo('c')
img.paste(img3, (0, 500))
img4 = draw_logo('k')
img.paste(img4, (500, 500))

plt.imshow(img)
plt.axis('off')
plt.show()
