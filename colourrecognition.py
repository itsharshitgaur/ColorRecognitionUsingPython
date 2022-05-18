# TOPIC - COLOUR RECOGNITION IN IMAGE

import cv2
import pandas as p

tap = False
r = g = b = xpos = ypos = 0

img = cv2.imread("colors.jpg")
img = cv2.resize(img, (900, 800))

index = ["colour", "colour_name", "hex", "R", "G", "B"]
csv = p.read_csv('colors.csv', names=index, header=None)


def getColourName(R, G, B):
    minimum = 1000
    for i in range(len(csv)):
        diff = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if diff <= minimum:
            minimum = diff
            cname = csv.loc[i, "colour_name"]
    return cname


def drf(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_MBUTTON:
        global b, g, r, xpos, ypos, tap
        tap = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', drf)

while 1:

    cv2.imshow("image", img)
    if tap:

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = getColourName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2)

        if r+g+b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2)
            
        tap = False

    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
