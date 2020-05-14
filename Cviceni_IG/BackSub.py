import cv2

cap = cv2.VideoCapture("./vid/video.avi")
cv2.namedWindow("Original Video", 1)
cv2.namedWindow("Foreground Mask by BGS KNN", 1)
cv2.namedWindow("Foreground Mask by BGS MOG2", 1)

BS1 = cv2.createBackgroundSubtractorKNN()
BS2 = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, Img = cap.read()

    if ret:
        fgmask1 = BS1.apply(Img)
        cv2.imshow('Foreground Mask by BGS KNN', fgmask1)

        fgmask2 = BS2.apply(Img)
        cv2.imshow('Foreground Mask by BGS MOG2', fgmask2)

        cv2.imshow("Original Video", Img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()