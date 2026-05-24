import cv2

def estimate_portion(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    total_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area

    if total_area < 5000:
        return "Small Portion"

    elif total_area < 15000:
        return "Medium Portion"

    else:
        return "Large Portion"