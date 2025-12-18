import matplotlib.pyplot as plt
from load_image import ft_load

array = []

def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    invertArr = array.copy()
    invertArr[:, :, 0] = 255 - array[:, :, 0]
    invertArr[:, :, 1] = 255 - array[:, :, 1]
    invertArr[:, :, 2] = 255 - array[:, :, 2]
    print("new : ", invertArr)
    plt.imshow(invertArr)
    plt.show()
    print("the shape is : ", invertArr.shape)
    return (invertArr)


def ft_red(array) -> array:
    """Only display red pixels"""
    # zSlice = slice(0,1)
    redFil = array.copy()
    redFil[:, :, 0] = array[:, :, 0]
    redFil[:, :, 1] = array[:, :, 1] * 0
    redFil[:, :, 2] = array[:, :, 2] * 0
    plt.imshow(redFil)
    plt.show()
    print("the shape is : ", redFil.shape)
    return (redFil)


def ft_green(array) -> array:
    """Only display green pixels"""
    # zSlice = slice(0,1)
    greenFil = array.copy()
    greenFil[:, :, 0] = 0
    greenFil[:, :, 1] = array[:, :, 1]
    greenFil[:, :, 2] = 0
    plt.imshow(greenFil)
    plt.show()
    print("the shape is : ", greenFil.shape)
    return (greenFil)


def ft_blue(array) -> array:
    """Only display blue pixels"""
    # zSlice = slice(0,1)
    blueFil = array.copy()
    blueFil[:, :, 0] = 0
    blueFil[:, :, 1] = 0
    blueFil[:, :, 2] = array[:, :, 2]
    plt.imshow(blueFil)
    plt.show()
    print("the shape is : ", blueFil.shape)
    return (blueFil)


def ft_grey(array) -> array:
    """Combine the 3 canals (rgb) to create a grey one.
    the real formula is : L = 0.299*R + 0.587*G + 0.114*B"""
    greyFil = array.copy()
    print(greyFil)
    greyFil2 = (greyFil[:, :, 0] + greyFil[:, :, 1] + greyFil[:, :, 2])/3

    greyFil[:, :, 0] = greyFil2[:, :]
    greyFil[:, :, 1] = greyFil2[:, :]
    greyFil[:, :, 2] = greyFil2[:, :]
    print(greyFil2)
    plt.imshow(greyFil)
    plt.show()


def main():
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

if (__name__ == "__main__"):
    main()

# def ft_red(array) -> array:
#     print(array)
#     tab = []
#     for i, line in enumerate(array) :
#         li = []
#         for px in line:
#             pxArr = []
#             for j, color in enumerate(px):
#                 # print("prev",color)
#                 if (j == 0):
#                     color = color
#                 else:
#                     color = color*0
#                 # print("next",color)
#                 pxArr.append(color)
#             li.append(pxArr)
#         tab.append(li)
#     invertArr = np.array(tab)

#     print("new : ",invertArr)
#     plt.imshow(invertArr)
#     plt.show()
#     return(invertArr)


# def ft_green(array) -> array:
#     print(array)
#     tab = []
#     for i, line in enumerate(array) :
#         li = []
#         for px in line:
#             pxArr = []
#             for j, color in enumerate(px):
#                 # print("prev",color)
#                 if (j == 1):
#                     color = color
#                 else:
#                     color = 0
#                 # print("next",color)
#                 pxArr.append(color)
#             li.append(pxArr)
#         tab.append(li)
#     invertArr = np.array(tab)

#     print("new : ",invertArr)
#     plt.imshow(invertArr)
#     plt.show()
#     return(invertArr)


# def ft_blue(array) -> array:
#     print(array)
#     tab = []
#     for i, line in enumerate(array) :
#         li = []
#         for px in line:
#             pxArr = []
#             for j, color in enumerate(px):
#                 # print("prev",color)
#                 if (j == 2):
#                     color = color
#                 else:
#                     color = 0
#                 # print("next",color)
#                 pxArr.append(color)
#             li.append(pxArr)
#         tab.append(li)
#     invertArr = np.array(tab)

#     print("new : ",invertArr)
#     plt.imshow(invertArr)
#     plt.show()
#     return(invertArr)

# def ft_grey(array) -> array:
#     print(array)
#     tab = []
#     for i, line in enumerate(array):
#         li = []
#         for px in line:
#             pxArr = []
#             for j, color in enumerate(px):
#                 color = px[0]
#                 print("next", color)
#                 pxArr.append(color)
#             li.append(pxArr)
#         tab.append(li)
#     invertArr = np.array(tab)
#     print("new : ", invertArr)
#     plt.imshow(invertArr)
#     plt.show()
#     return (invertArr)


# def ft_invert(array) -> array:
#     print(array)
#     tab = []
#     for i, line in enumerate(array) :
#         li = []
#         for px in line:
#             pxArr = []
#             for color in px:
#                 # print("prev",color)
#                 color = 255 - color
#                 # print("next",color)
#                 pxArr.append(color)
#             li.append(pxArr)
#         tab.append(li)
#     invertArr = np.array(tab)
