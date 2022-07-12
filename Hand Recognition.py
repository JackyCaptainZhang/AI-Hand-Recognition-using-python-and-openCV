import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
LM_Style = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=3)
Line_Style = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)
pTime = 0
cTime = 0
d = 0
dd = 0

while True:
    switch, img = cap.read()
    if switch:
        img = cv.flip(img, 1)
        img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        processed_hands = hands.process(img_RGB)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        if processed_hands.multi_hand_landmarks:
            for item in processed_hands.multi_hand_landmarks:
                # print(type(item))
                # print(item)
                # print(type(processed_hands.multi_hand_landmarks))
                mpDraw.draw_landmarks(img, item, mpHands.HAND_CONNECTIONS, LM_Style, Line_Style)
                for i, lm in enumerate(item.landmark):
                    xAxis = round(imgWidth * lm.x, 1)
                    yAxis = round(imgHeight * lm.y, 1)
                    cv.putText(img, str(i), (int(xAxis) - 23, int(yAxis) + 5), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)
                    print(i, xAxis, yAxis)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img, f"FPS : {int(fps)}", (10, 35), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        cv.imshow('Cam', img)
    if cv.waitKey(1) == ord('q'):
        break