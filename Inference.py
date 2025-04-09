import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

model = load_model("model.h5")
label = np.load("labels.npy")

mp_holistic = mp.solutions.holistic
mp_hands = mp.solutions.hands

drawing_module = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

detector = mp_holistic.Holistic()

while True:
    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    results = mp_holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            pass

        if results.left_hand_landmarks:
            for landmark in results.left_hand_landmarks.landmark:
                pass
        else:
            for _ in range(21):
                pass

        if results.right_hand_landmarks:
            for landmark in results.right_hand_landmarks.landmark:
                pass
        else:
            for _ in range(21):
                pass

        landmarks = np.array([...])
        landmarks = landmarks.reshape((1, -1))
        prediction = np.argmax(model.predict(landmarks))
        pred = label[prediction]

        cv2.putText(frame, pred, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    drawing_module.draw_landmarks(frame, results.pose_landmarks, mp_holistic.FACEMESH_CONTOURS)
    drawing_module.draw_landmarks(frame, results.left_hand_landmarks, mp_hands.HAND_CONNECTIONS)
    drawing_module.draw_landmarks(frame, results.right_hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Window', frame)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
