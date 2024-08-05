import os
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "55"
HEIGHT_CM = "170"
AGE = "21"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint  = "https://api.sheety.co/8c7d2aeefdfc4e209ed4eb51b3178acf/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
results = response.json()
print(response.text)
print(results)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in results["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": "Bearer RUNTIMEERROR"
    }

    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
