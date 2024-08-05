import requests

SHEETY_ENDPOINT = "https://api.sheety.co/8c7d2aeefdfc4e209ed4eb51b3178acf/flightDeals/users"
bearer_headers = {
    "Authorization": "Bearer Hurriyet"
}
print("Welcome to the Flight Club!")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
email_confirm = input("Type your email again. ")
if email == email_confirm:
  print("You're in the club!")
else:
  print("Emails don't match. Try again.")
new_data = {
  "user": {
    "firstName": first_name,
    "lastName": last_name,
    "email": email
  }
}
response = requests.post(url=SHEETY_ENDPOINT, json=new_data, headers=bearer_headers)
print(response.text)

