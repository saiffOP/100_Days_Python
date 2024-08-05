import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/8c7d2aeefdfc4e209ed4eb51b3178acf/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/8c7d2aeefdfc4e209ed4eb51b3178acf/flightDeals/users"

bearer_headers = {
        "Authorization": "Bearer Hurriyet"
    }

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destinations_code(self):
        for city in self.destination_data:
            new_data = {
                "price":  {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers,
            )
            print(response.text)

    def get_customers_email(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(
            url=customers_endpoint,
            headers=bearer_headers
        )
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
