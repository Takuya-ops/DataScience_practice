import mediapipe as mp
import cv2

# MediapipeのHandモジュールを初期化
mp_hands = mp.solutions.hands

# カメラからのキャプチャを開始
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break

    # 画像をRGBに変換してHandモデルに渡す
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.Hands().process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 手のポイントを描画
            for point in mp_hands.HandLandmark:
                x = int(hand_landmarks.landmark[point].x * image.shape[1])
                y = int(hand_landmarks.landmark[point].y * image.shape[0])
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    # 画像を表示
    cv2.imshow("Hand Tracking", image)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
