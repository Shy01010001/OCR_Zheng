# -*- coding: utf-8 -*-
"""
Created on Mon May  1 08:49:01 2023

@author: youjingyi
"""

import os
import requests
from bs4 import BeautifulSoup

# 创建一个用于保存新闻文本文件的目录
if not os.path.exists("yahoo_news_articles"):
    os.mkdir("yahoo_news_articles")

url = "https://news.yahoo.co.jp/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers, verify=False)  # 禁用SSL验证
soup = BeautifulSoup(response.text, "html.parser")

# 查找新闻链接
news_links = soup.find_all("a", class_="newsFeed_item_link")

for link in news_links:
    article_url = link["href"]
    article_response = requests.get(article_url, headers=headers, verify=False)  # 禁用SSL验证
    article_soup = BeautifulSoup(article_response.text, "html.parser")

    # 提取新闻标题以用作文件名
    title = article_soup.find("h1", class_="newsTitle").text.strip()
    file_name = f"yahoo_news_articles/{title}.txt"

    # 提取文章段落
    paragraphs = article_soup.find_all("p", class_="articleParagraph")

    with open(file_name, "w", encoding="utf-8") as file:
        for paragraph in paragraphs:
            file.write(paragraph.text.strip() + "\n")

print("新闻爬取完成")
