from bs4 import BeautifulSoup
import requests
import smtplib
import os

MY_EMAIL = "shirgaonkarsaif2786@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

# with open(file="website.html", encoding="utf-8") as data:
#     contents = data.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
articles_texts = []
articles_links = []
for article in articles:
    text = article.a.getText()
    articles_texts.append(text)
    link = article.a.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="saifshirgaonkar1786@gmail.com",
        msg=f"Subject:Today's Trending Tech News\n\n{articles_texts[largest_index]}\n{articles_links[largest_index]}"
    )
# for article in articles:
#     article_text = article.a.getText()
#     article_link = article.a["href"]
#
#     for article_upvote in article_upvotes:
#         if article_upvote:
#             article_upvote = article_upvote.getText()
#         else:
#             article_upvote = "N/A"
#
#         print("Article Text:", article_text)
#         print("Article Link:", article_link)
#         print("Article Upvote:", article_upvote)
#         print("\n")
#         del article_upvotes[0]
#         break
