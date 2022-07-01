from bs4 import BeautifulSoup
import requests

response= requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
#all_a_titles = soup.find_all(class_="storylink")
#print(all_a_titles)

article_tag = soup.find(name="a", class_="titlelink")
print(article_tag)

all_articles_tag = soup.find_all(name="a", class_="titlelink")
for titles in all_articles_tag:
    print(titles.getText())

article_link = article_tag.get("href")
print(article_link)
updoots = soup.find(name = "span", class_="score")
print(updoots)
# let's grab all the titles
