from PIL import Image
from typing import Callable, Tuple


class Filterizer:
    @staticmethod
    def apply(image: Image, simple_filter: Callable[[Tuple[int, ...]], Tuple[int, ...]]):
        width = image.size[0]
        height = image.size[1]

        for y in range(height):
            for x in range(width):
                color = image.getpixel((x, y))
                image.putpixel((x, y), simple_filter(color))


class SimpleFilter:
    @staticmethod
    def atmosphere(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return (color[1] + color[2]) // 2, (color[0] + color[2]) // 2, (color[0] + color[1]) // 2

    @staticmethod
    def blacklight(color: Tuple[int, ...]) -> Tuple[int, ...]:
        luminance = (222 * color[0] + 707 * color[1] + 71 * color[2]) / 1000
        fx_weight = 2
        return tuple((min(int(abs(c - luminance) * fx_weight), 255) for c in color))

    @staticmethod
    def burn(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = sum(color) // 3
        return min(grey * 3, 255), grey, grey // 3

    @staticmethod
    def color_shift(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return color[2], color[0], color[1]

    @staticmethod
    def freeze(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple((min(int(abs((color[i] - color[(i + 1) % 3] - color[(i + 2) % 3]) * 1.5)), 255) for i in range(3)))

    @staticmethod
    def lava(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return sum(color) // 3, abs(color[2] - 128), abs(color[2] - 128)

    @staticmethod
    def metal(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = (color[0] * 222 + color[1] * 707 + color[2] * 71) // 1000
        return min(2 * (grey + 70) - 128, 255), min(2 * (grey + 65) - 128, 255), min(2 * (grey + 75) - 128, 255)

    @staticmethod
    def negative(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple((255 - c for c in color))

    @staticmethod
    def ocean(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = sum(color) // 3
        return grey // 3, grey, min(grey * 3, 255)



class GrayscaleFilter:
    @staticmethod
    def average(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = sum(color) // 3
        return grey, grey, grey

    @staticmethod
    def binary(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = sum(color) / 3
        if grey > (255 / 2):
            grey = 255
        else:
            grey = 0

        return grey, grey, grey

    @staticmethod
    def blue_channel(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return color[2], color[2], color[2]

    @staticmethod
    def desaturation(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = (max(color) + min(color)) // 2
        return grey, grey, grey

    @staticmethod
    def green_channel(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return color[1], color[1], color[1]

    @staticmethod
    def luminance(color: Tuple[int, ...]) -> Tuple[int, ...]:
        grey = int(color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114)
        return grey, grey, grey

    @staticmethod
    def red_channel(color: Tuple[int, ...]) -> Tuple[int, ...]:
        return color[0], color[0], color[0]


if __name__ == "__main__":
    simple_filters = [
        (SimpleFilter.atmosphere, "atmosphere"),
        (SimpleFilter.blacklight, "blacklight"),
        (SimpleFilter.burn, "burn"),
        (SimpleFilter.color_shift, "color_shift"),
        (SimpleFilter.freeze, "freeze"),
        (SimpleFilter.lava, "lava"),
        (SimpleFilter.metal, "metal"),
        (SimpleFilter.negative, "negative"),
        (SimpleFilter.ocean, "ocean"),
    ]

    grayscale_filters = [
        (GrayscaleFilter.average, "average"),
        (GrayscaleFilter.binary, "binary"),
        (GrayscaleFilter.blue_channel, "blue_channel"),
        (GrayscaleFilter.desaturation, "desaturation"),
        (GrayscaleFilter.green_channel, "green_channel"),
        (GrayscaleFilter.luminance, "luminance"),
        (GrayscaleFilter.red_channel, "red_channel"),
    ]

    for photo_filter in simple_filters:
        image = Image.open("chameleon.jpg")
        Filterizer.apply(image, photo_filter[0])
        image.save(f"filterized/simple/{photo_filter[1]}.jpg")

    for photo_filter in grayscale_filters:
        image = Image.open("chameleon.jpg")
        Filterizer.apply(image, photo_filter[0])
        image.save(f"filterized/grayscale/{photo_filter[1]}.jpg")
