import os
import requests
import smtplib
from datetime import datetime, timedelta

MY_EMAIL = "shirgaonkarsaif2786@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
news_api_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_api_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday = datetime.now() - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
day_before_yesterday = day_before_yesterday.strftime('%Y-%m-%d')
yesterday_price = float(stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])

day_before_yesterday_price = float(stock_data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])


difference = yesterday_price - day_before_yesterday_price
diff_percentage = abs(round((difference / yesterday_price) * 100))
sign = None
if difference > 0:
    sign = "+"
else:
    sign = "-"
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"]
three_articles = news_data[:3]

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
articles_list = [f"{STOCK}: {sign}{diff_percentage}%\nHeadline: {article['title']}. \n Brief: {article['description']}"
                 for article in three_articles]
# Optional: Format the SMS message like this:
if diff_percentage >= 1:
    for article in articles_list:
        article = article.encode('ascii', 'ignore').decode('ascii')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="saifshirgaonkar1786@gmail.com",
                msg=f"Subject: Stock News!\n\n{article}"
            )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
"""
