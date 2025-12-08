from load_image import ft_load
from PIL import Image
import numpy as np

def zoom():
    arr = ft_load("animal.jpeg")
    print(arr)
    img = Image.open("animal.jpeg").convert('L')
    arr2 = np.array(img)
    ySlice = slice(100, 500)
    xSlice = slice(450, 850)
    cSlice = slice(0,1)
    zoomed2=arr2[ySlice, xSlice]
    
    
    zoomed = arr[ySlice, xSlice, cSlice]
    print(f"New shape after slicing: {zoomed.shape} or {zoomed2.shape}")
    print(zoomed)

    zoomed=arr2[ySlice, xSlice]
    img = Image.fromarray(zoomed)
    img.show()


def main():
    zoom()


if (__name__ == "__main__"):
    main()