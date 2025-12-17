from load_image import ft_load
import matplotlib.pyplot as plt


def zoom():
    """
    This function takes no parameter. Calls the
    function ft_load to get an px array of the
    image. Create a new slice to get the head and put it
    in the array. Remove the last dimension to get a 2D arr.

    plt.imshow interpret the value in the arr as color and
    prepare them to be displayed
    plt.show() --> show the img
    """

    arr = ft_load("animal.jpg")
    if (arr is None):
        return
    print(arr)
    ySlice = slice(100, 500)
    xSlice = slice(450, 850)
    # 1 canal.
    cSlice = slice(0, 1)
    # intensity of the coulor chosen
    zoomed = arr[ySlice, xSlice, cSlice]
    # remove the last dimension no canal, usefull for grayscale (2D array)
    # when we put an index integer we remove the dimension
    zoomed_gray = zoomed[:, :, 0]

    print(f"New shape after slicing: {zoomed.shape} or {zoomed_gray.shape}")
    print(zoomed)

    plt.imshow(zoomed_gray, cmap="gray")
    # plt.colorbar()
    plt.show()


def main():
    zoom()


if (__name__ == "__main__"):
    main()
