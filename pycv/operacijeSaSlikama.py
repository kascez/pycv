import cv2

img = cv2.imread('messi5.jpg')

print(img.shape) #redovi kolone i kanali
print(img.size) #broj piksela
print(img.dtype) #vrata tip podataka - uint8
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)
cv2.waitKey(9000)
cv2.destroyAllWindows()