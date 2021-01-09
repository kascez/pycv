import cv2

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0, 0), (255, 255), (145, 98, 43), 10) #prava linija
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10) #linija sa strelicom

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1) #popunjen pravouganokin
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1) #zeleni krug

font = cv2.FONT_HERSHEY_SIMPLEX #izbor fonta
img = cv2.putText(img, 'Simulacije', (10, 500), font, 2, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

