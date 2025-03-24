from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
site_text = response.text
soup = BeautifulSoup(site_text, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")
article_links = []
article_scores = []
for article in articles:
    article_links.append(article.select_one("a").get("href"))
for score in scores:
    article_scores.append(int(score.getText().split(" ")[0]))

largest_score_index = article_scores.index(max(article_scores))

print(article_scores[largest_score_index])
first_article_score = soup.find(name="span", class_="score").getText()

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")

#Notes on this module****
#soup = all the html for the page
#soup.prettify() = all the html, with indentations
#soup.title = "<title>Site title</title>"
#soup.title.name = "title"
#soup.title.string = "Site title"
#soup.a = first anchor tag
#soup.p = first p tag
#a.getText() = get the text of a tag
#a.get("href") = get the link of an anchor tag
#a.get("class") = get the class

#soup.find(name="h1", id="name") find a tag by id
#soup.find(name="h3", class_="heading) find a tag by class, has to be "class_"
#soup.find_all() = find all tags of a kind
#soup.find_all(a) = list of all anchor tags

#soup.select() = all matching items
#soup.select_one() = first matching item

#soup.select_one(selector="p a") just like using css selectors
#soup.select_one("#name") also works

#soup.select(".heading")  select the class
#
#
#
# print(soup.title.string)