#import the libraries
import cv2
import numpy as no
import mediapipe 
import pyautogui #PyAutoGui


hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
x1 = y1 = x2 = y2 = 0

camera = cv2.VideoCapture(0)
while True:
    _,image = camera.read()
    height, width, _ = image.shape
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = hands.process(rgb_image)

    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * width)
                y = int(lm.y * height)
                print(x, y)
                if id == 8:
                    mouse_x = int(screen_width / width  * x)
                    mouse_y = int(screen_height / height  * y)
                    cv2.circle(image, (x,y), 8, (230, 230, 250))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(image, (x,y), 8, (230, 230, 250))
        dist = y2 - y1
        print(dist)
        if(dist < 25):
            pyautogui.click()
    cv2.imshow("Hand Track", image)

    key = cv2.waitKey(100)
    if key == 27: 
        break
camera.release()
cv2.destroyAllWindows()