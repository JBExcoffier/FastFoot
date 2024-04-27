import requests
from bs4 import BeautifulSoup
from data.parse.parse_eurosport import *


def get_articles_eurosport_football():
    URL = "https://www.eurosport.com/" + "football" + "/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    main_articles = []

    try:
        first_article = get_first_article_infos(soup=soup)
        main_articles.append(first_article)
    except Exception as e:
        print(e)

    try:
        second_articles = get_second_articles(soup=soup)
    except Exception as e:
        print(e)
        second_articles = []

    for sa in second_articles:
        try:
            main_articles.append(get_second_article_infos(soup=sa))
        except Exception as e:
            print(e)

    if main_articles:
        return main_articles

    raise ValueError("No article was correctly parsed in the desired format.")
