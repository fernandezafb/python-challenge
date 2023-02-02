

from PIL import Image


# Construct two different images with even/odd (width + height) pixels
def run_challenge():
    image = Image.open('cave.jpeg')
    (width, height) = image.size

    even = Image.new('RGB', [width // 2, height // 2])
    odd = Image.new('RGB', [width // 2, height // 2])

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            if (i + j) % 2 == 0:
                even.putpixel((i // 2, j // 2), pixel)
            else:
                odd.putpixel((i // 2, j // 2), pixel)

    even.show()
    odd.show()

    image.close()


if __name__ == '__main__':
    run_challenge()
