from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BOM"


if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destinations_code()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination_code in destinations:
    try:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination_code,
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight is None:
            continue

        if flight.price < destinations[destination_code]["price"]:
            users = data_manager.get_customers_email()
            print(users)
            emails = [row.get("email", "N/A") for row in users]
            names = [row.get("firstname", "N/A") for row in users]

            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                      f" to {flight.destination_city}-{flight.destination_airport}," \
                      f" from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)

            notification_manager.send_mail(
                emails,
                message=message
            )
    except IndexError as e:
        print(f"Error checking flights for destination {destination_code}: {e}")