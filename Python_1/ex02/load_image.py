from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str):
    """
    It takes a path as parameter and return an array
    containing RGB'value of each pixel.of the image with the  of each px
    .convert is used to force the image
     to have always 3 canals
    .shape displays : height, weight and number of canals, 3 is for RGB"
    """
    try:
        if path == "":
            raise ValueError("ValueError: Empty path")
        with Image.open(path) as image:
            img = image.convert('RGB')
            imgPixRGB = np.array(img)
            result = imgPixRGB
            print("The shape of image is:", np.array(img).shape)
            return (result)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except ValueError as e:
        print(e)
    except UnidentifiedImageError:
        print("Not the right format to open : JPEG, JPG")


def main():
    print(ft_load("landscape.jpeg"))
    print(ft_load("landscape.jpg"))
    print(ft_load(""))
    print(ft_load("animal.jpeg"))
    print(ft_load("huh-cat.mp4"))


if (__name__ == "__main__"):
    main()
