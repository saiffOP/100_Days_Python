import requests
import smtplib

MY_EMAIL = "shirgaonkarsaif2786@gmail.com"
PASSWORD = "dugmvsmzlvzajpvx"

api_key = "f67baffa2cea3b07a53f81f3683f4eb0"

parameters = {
    "lat": 17.9816227,
    "lon": 73.0530605,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for hour_data in data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="saifshirgaonkar1786@gmail.com",
            msg="Subject: Rain Alert\n\nIt's going to rain today. Make sure to bring an Umbrella."
        )
else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="saifshirgaonkar1786@gmail.com",
            msg="Subject: Rain Alert\n\nIt's not going to rain today."
        )
