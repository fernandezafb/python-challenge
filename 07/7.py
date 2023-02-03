
import png
import urllib.request


# Recommended to use Pillow library instead: https://pypi.org/project/Pillow/.
def process_image():
    reader = png.Reader(file=urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png'))
    print(reader.asRGBA())

    # Rows is an iterator containing RGBA values of the like [r, g, b, a, r, g, b, a...] but as bytearrays
    # RGB values for grey colors are equal: https://www.w3schools.com/colors/colors_shades.asp
    (width, height, rows, info) = reader.read()

    # Rows is a interator (generator object)
    byte_arrays = [row for row in rows]

    # The grey row we want to analyze is going to be around the middle
    mid = len(byte_arrays) // 2
    row = [bytes for bytes in byte_arrays[mid]]

    # The number 7 is the amount of pixel of the same grey color in the image
    # This can be seen in the mid RGB pixels, they are repeated 7 times each grey color 
    print(''.join([chr(row[pos]) for pos in range(0, len(row), 7) if row[pos] == row[pos+1] == row[pos+2]]))

    # Final message contains the solution:
    solution = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print(''.join([chr(value) for value in solution]))


if __name__ == '__main__':
    process_image()
