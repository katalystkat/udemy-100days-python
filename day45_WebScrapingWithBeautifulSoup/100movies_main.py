from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text
soup = BeautifulSoup(movies_web_page, "html.parser")

#Highlight direct text that we want to capture and "inspect element" to identify the exact tags/names that we want to use to identify all movie names 
all_movies= soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")\

print(movies)
