import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def main():
	arr = ft_load("animal.jpeg")
	if (arr is None):
		return (1)
	ySlice = slice(100, 500)
	xSlice = slice(450, 850)
    # 1 canal.
	cSlice = slice(0, 1)
    # intensity of the coulor chosen
	zoomed = arr[ySlice, xSlice, cSlice]
	zoomed_gray = zoomed[:, :, 0]
	print(f"The shape of image is: {zoomed.shape} or {zoomed_gray.shape}")
	print(zoomed)
	
	print(zoomed_gray)
	# print(trans)
	
	# transpose : i ligne et j colonne

	#tranArr = np.array()
	for line in zoomed_gray:
		for elmt in line:
			print(elmt)

	plt.imshow(zoomed_gray, cmap="gray")
	plt.show()




if (__name__== "__main__"):
	main()