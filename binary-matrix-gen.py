import cv2
import numpy as np

figureImage = cv2.imread("figure.png", cv2.IMREAD_GRAYSCALE)

# change values to adjust rows and columsn of matrix
newWidth = 3
newHeight = 3

resizedImage = cv2.resize(figureImage, (newWidth, newHeight))

# Apply thresholding to create a binary image
_, binaryImage = cv2.threshold(resizedImage, 128, 255, cv2.THRESH_BINARY)

# Convert the binary image to a 2x2 binary matrix
binaryMatrix = (binaryImage > 0).astype(int)

# Define the file name for saving the binary matrix
fileName = "binary-matrix.txt"

# Save the binary matrix to a text file
with open(fileName, "w") as file:
    for row in binaryMatrix:
        file.write(" ".join(map(str, row)) + "\n")

print("Binary matrix saved to", file_name)
