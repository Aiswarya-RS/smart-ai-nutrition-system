import requests

APP_ID = "your_app_id"
API_KEY = "your_api_key"

def get_nutrition(food_name):

    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "query": food_name
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    try:
        food = result['foods'][0]

        nutrition = {
            "Calories": food['nf_calories'],
            "Protein": food['nf_protein'],
            "Carbs": food['nf_total_carbohydrate'],
            "Fat": food['nf_total_fat']
        }

        return nutrition

    except:
        return "Nutrition data not found"