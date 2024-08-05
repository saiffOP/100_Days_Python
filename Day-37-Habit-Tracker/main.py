import requests
from datetime import datetime


TOKEN = "jsycabuq7wd"
USERNAME = "saifsgkr"
GRAPH_ID = "pushupgraph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Push Ups Graph",
    "unit": "reps",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

add_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "24",
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)

# update_pixel_endpoint = f"{add_pixel_endpoint}/{today.strftime('%Y%m%d')}"
#
# update_pixel_params = {
#     "quantity": "30"
# }
#
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

