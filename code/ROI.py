import cv2
from cvzone import HandTrackingModule


cnt_img=0 

detector = HandTrackingModule.HandDetector()

capture = cv2.VideoCapture(0)


while True:
    ret,frame = capture.read()
    img_copy = frame.copy()
    hands, frame = detector.findHands(frame)

    frame = cv2.flip(frame, 1) 

    cv2.imshow("Image", frame)

    key = cv2.waitKey(1) & 0xFF
    # Quit
    if key == 27:
        print("quit...")
        break

    bbox_value = hands[0].get('bbox')

    roi = img_copy[bbox_value[1]:bbox_value[1] + bbox_value[3], bbox_value[0]:bbox_value[0] + bbox_value[2]]
    cnt_img += 1



capture.release()
cv2.destroyAllWindows() 