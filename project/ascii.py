from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str, default="ascii_dora.png")
parser.add_argument("-o", "--output", type=str, default="output.txt")

parser.add_argument("--width", type=int, default=80)
parser.add_argument("--height", type=int, default=80)

args = parser.parse_args()

img = args.file
width = args.width
height = args.height
output = args.output

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)


def getchar(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length

    return ascii_char[int(gray / unit)]


def main():
    im = Image.open(img)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""

    for i in range(height):
        for j in range(width):
            txt += getchar(*im.getpixel((j, i)))
        txt += "\n"

        print(txt)

    if output:
        with open(output, "w") as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)


if __name__ == "__main__":
    main()
