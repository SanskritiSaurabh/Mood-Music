import numpy as np
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    results = mp.solutions.holistic.Holistic().process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.face_landmarks:
        landmark_points = []
        for landmark in results.face_landmarks.landmark:
            landmark_points.append(landmark.x - results.face_landmarks.landmark[1].x)
            landmark_points.append(landmark.y - results.face_landmarks.landmark[1].y)

        if results.left_hand_landmarks:
            hand_points = []
            for landmark in results.left_hand_landmarks.landmark:
                hand_points.append(landmark.x - results.left_hand_landmarks.landmark[8].x)
                hand_points.append(landmark.y - results.left_hand_landmarks.landmark[8].y)
        else:
            hand_points = [0.0] * 42
        landmark_points.extend(hand_points)

        if results.right_hand_landmarks:
            hand_points = []
            for landmark in results.right_hand_landmarks.landmark:
                hand_points.append(landmark.x - results.right_hand_landmarks.landmark[8].x)
                hand_points.append(landmark.y - results.right_hand_landmarks.landmark[8].y)
        else:
            hand_points = [0.0] * 42
        landmark_points.extend(hand_points)

        frame = mp.solutions.drawing_utils.draw_landmarks(frame, results.face_landmarks, mp.solutions.holistic.FACEMESH_CONTOURS)
        frame = mp.solutions.drawing_utils.draw_landmarks(frame, results.left_hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
        frame = mp.solutions.drawing_utils.draw_landmarks(frame, results.right_hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

        cv2.putText(frame, str(data_size), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

    cv2.imshow("window", frame)
    if cv2.waitKey(1) == 27 or data_size > 99:
        cv2.destroyAllWindows()
        cap.release()
        break

X = []
data_size = 0
for _ in range(100):
    landmark_points = []
    frame = cap.read()[1]
    frame = cv2.flip(frame, 1)
    results = mp.solutions.holistic.Holistic().process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.face_landmarks:
        for landmark in results.face_landmarks.landmark:
            landmark_points.append(landmark.x - results.face_landmarks.landmark[0].x)
            landmark_points.append(landmark.y - results.face_landmarks.landmark[0].y)

        if results.left_hand_landmarks:
            for landmark in results.left_hand_landmarks.landmark:
                landmark_points.append(landmark.x - results.left_hand_landmarks.landmark[8].x)
                landmark_points.append(landmark.y - results.left_hand_landmarks.landmark[8].y)
        else:
            landmark_points.extend([0.0] * 42)
        if results.right_hand_landmarks:
            for landmark in results.right_hand_landmarks.landmark:
                landmark_points.append(landmark.x - results.right_hand_landmarks.landmark[8].x)
                landmark_points.append(landmark.y - results.right_hand_landmarks.landmark[8].y)
        else:
            landmark_points.extend([0.0] * 42)
        X.append(landmark_points)
        data_size += 1

import matplotlib.pyplot as plt
plt.plot(np.array(X).T)
plt.show()
