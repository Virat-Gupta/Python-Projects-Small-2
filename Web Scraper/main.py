from bs4 import BeautifulSoup
import requests
#import lxml : for certain websites , use BeautifulSoup(contents, 'lxml')

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
title_list =[title.find("a").text for title in soup.select(selector=".titleline")]
article_link_list = [title.find("a").get("href") for title in soup.select(selector=".titleline")]
score_list = [int(score.text.split(" ")[0]) for score in soup.select(selector=".subtext .score")]
ad_index = [article_link_list.index(link) for link in article_link_list if ("ycombinator" in link)]
# print(ad_index)
for index in ad_index:
    # print("-----")
    # print(article_link_list[index])
    article_link_list.remove(article_link_list[index])
    # print(article_link_list[index])
    # print("-----")

    title_list.remove(title_list[index])
max_upvote = score_list.index(max(score_list))
print(score_list)
print(max_upvote)
print(article_link_list[max_upvote])
print(title_list[max_upvote])
print(score_list[max_upvote])

# for i in range (0,10):
#     print(f"{title_list[i]}  :  {score_list[i]}")