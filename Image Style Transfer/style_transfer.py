import cv2

image = cv2.imread("image.jpg")

stylized = cv2.stylization(image, sigma_s=60, sigma_r=0.6)

cv2.imwrite("output.jpg", stylized)

print("Stylized image saved as output.jpg")