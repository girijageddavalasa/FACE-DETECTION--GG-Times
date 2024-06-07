# Face Detection with OpenCV

This project demonstrates basic face detection using OpenCV's Haar Cascade Classifier. The provided code reads an image, detects faces, and displays the result with rectangles drawn around the detected faces.

# Requirements
     Python 3.x
     OpenCV library
# Installation
       Install Python from python.org.
   install cv2 module
        pip install opencv-python
# Explanation
     haarcascade_frontalface_default.xml: The Haar Cascade XML file for frontal face detection.
    cv2.CascadeClassifier(alg): Loads the Haar Cascade algorithm.
    cv2.imread(image): Reads the image file.
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): Converts the image to grayscale.
    haar_cascade.detectMultiScale(grayimg, 1.3, 10): Detects faces in the grayscale image.
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2): Draws a red rectangle around detected faces.
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 150, 20), 2): Adds text indicating whether a face is detected.
    cv2.imshow("FACE DETECTION", img): Displays the image with the detected faces.
    cv2.waitKey(10): Waits for a key press to break the loop.
# Notes

    Ensure that the haarcascade_frontalface_default.xml file is in the same directory as your script or provide the correct path.
    Press the 'ESC' key to exit the image display window.
