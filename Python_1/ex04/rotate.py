import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def main():
    """
    This program load an image, square it and without using
    the transpose function, transpose the array.
    """
    arr = ft_load("animal.jpeg")
    if (arr is None):
        return (1)
    # ySlice = slice(100, 500)
    # xSlice = slice(450, 850)
    # # 1 canal.
    # cSlice = slice(0, 1)
    # intensity of the coulor chosen
    # zoomed = arr[ySlice, xSlice, cSlice]
    zoomed = arr[100:500, 450:850, 0:1]
    zoomed_gray = zoomed[:, :, 0]
    print(f"The shape of image is: {zoomed.shape} or {zoomed_gray.shape}")
    print(zoomed)

    tab = []

    for i, col in enumerate(zoomed_gray[0]):
        ligne = []
        for line in zoomed_gray:
            ligne.append(line[i])
        tab.append(ligne)

    tranArr = np.array(tab)
    print("New shape after Transpose:", tranArr.shape)
    print(tranArr)

    plt.imshow(tranArr, cmap="gray")
    plt.show()


if (__name__ == "__main__"):
    main()
