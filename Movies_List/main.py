import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).text, "html.parser")

#movie titles are under <h2> <strong>

titles = soup.select(selector="h2 strong")

names = []
for title in titles:
    names.append(title.getText().split(" ", 1)[1].strip())
names.reverse()

with open("movies.txt", mode="w") as file:
    for name in names:
        file.write(f"{name}\n")