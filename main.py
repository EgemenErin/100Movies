import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
WEBSITE = requests.get(URL)
SOUP = BeautifulSoup(WEBSITE.text, "html.parser")
TITLES = SOUP.find_all("h3",{"class":"title"})
TITLE_NAMES = [title.get_text() for title in TITLES]
for i in range(len(TITLE_NAMES) - 1, -1, -1):
    print(TITLE_NAMES[i])

