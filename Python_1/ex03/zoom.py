from load_image import ft_load
import matplotlib.pyplot as plt


def zoom():
    arr = ft_load("animal.jpeg")
    print(arr)
    ySlice = slice(100, 500)
    xSlice = slice(450, 850)
    # 1 canal
    cSlice = slice(0, 1)
    zoomed = arr[ySlice, xSlice, cSlice]
    zoomed_gray = zoomed[:, :, 0]
    # remove the last dimension no canal, usefull for grayscale
    print(f"New shape after slicing: {zoomed.shape} or {zoomed_gray.shape}")
    print(zoomed)

    plt.imshow(zoomed_gray, cmap="gray")
    # plt.colorbar()
    plt.show()


def main():
    zoom()


if (__name__ == "__main__"):
    main()
