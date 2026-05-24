from webcam_capture import start_webcam
from food_detector import detect_food
from portion_estimator import estimate_portion
from nutrition_api import get_nutrition
from voice_assistant import speak
from utils import print_nutrition

# Step 1: Capture image
start_webcam()

image_path = "captured_food.jpg"

# Step 2: Detect food
foods = detect_food(image_path)

print("\nDetected Foods:", foods)

speak(f"Detected foods are {', '.join(foods)}")

# Step 3: Portion estimation
portion = estimate_portion(image_path)

print("Portion Size:", portion)

speak(f"Estimated portion is {portion}")

# Step 4: Nutrition analysis
for food in foods:

    nutrition = get_nutrition(food)

    print(f"\nNutrition for {food}")

    if isinstance(nutrition, dict):
        print_nutrition(nutrition)

        speak(
            f"{food} contains "
            f"{nutrition['Calories']} calories"
        )

    else:
        print(nutrition)