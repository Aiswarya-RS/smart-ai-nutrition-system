import cv2

def start_webcam():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Smart Nutrition Scanner", frame)

        key = cv2.waitKey(1)

        # Press S to save image
        if key == ord('s'):
            cv2.imwrite("captured_food.jpg", frame)
            print("Image Captured")
            break

    cap.release()
    cv2.destroyAllWindows()