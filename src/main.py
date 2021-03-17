# Importing openCV
import cv2

# Getting video input for webcam. The int argument sets de index of the cam to be used.
video = cv2.VideoCapture(1)

# Resizing output image
cv2.namedWindow("Capturing", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Capturing", 512, 288)

# Importing trained Haar cascade classifier (HCC)
cascade_man = cv2.CascadeClassifier('..\\data\\Man\\Cascade\\cascade.xml')

# Main loop to get frames from the video source
while True:
    # Reading frame
    check, frame = video.read()

    # Getting rectangles from HCC
    rectangles = cascade_man.detectMultiScale(frame, minSize = (50, 50))

    # Drawing rectangles and labels
    for (x,y,w,h) in rectangles:
        cv2.putText(img = frame, text = "PEPE", org = (x, y - 7), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (0, 255, 0), thickness=2)
        cv2.rectangle(img = frame, pt1 = (x,y), pt2 = (x + w, y + h), color = (0, 255, 0), thickness = 2)

    # Showing output frame
    cv2.imshow("Capturing", frame)

    # Exit loop if 'Q' key is pressed on the keyboard
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Close video capturing 
video.release()

# Close all windows opened by this script
cv2.destroyAllWindows