from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
moive_web_scrape = response.text

soup = BeautifulSoup(moive_web_scrape, "html.parser")

movie_list = [movie.text for movie in soup.find_all("h3")]

with open(r"Web Scraper\movie.txt","w", encoding="utf-8") as file :
    for movie in movie_list[::-1]:
        file.write(movie)
        file.write("\n")