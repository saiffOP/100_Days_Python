from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                            "/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]

hundred_movies_list = [movies_list[len(movies_list) - i] for i in range(1, len(movies_list)+1)]
hundred_movies_list[11] = "12) The Godfather Part II"
structured_movies = []
for movie in hundred_movies_list:
    movie = movie.split(")")
    new_movie = movie[1]
    structured_movies.append(new_movie)

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for ranking, movie in enumerate(structured_movies, start=1):
        file.write(f"{ranking}) {movie}\n")

