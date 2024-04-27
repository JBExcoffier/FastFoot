import requests
from bs4 import BeautifulSoup


def get_intro_article_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup.find_all(class_="mb-5 text-onLight-02 caption-s3-fx")[0].getText()


def get_first_article_infos(soup):
    res = {"title": None, "link": None}

    main_article = soup.find_all(
        class_="card-hover relative h-full overflow-hidden lg:rounded-[4px]"
    )[0]

    res["title"] = main_article.find_all(
        class_="card-hover-underline font-bold -md:caps-s3-fx md-lg:caps-s3-fx lg:caps-s2-fx -md:lines-3 md-lg:lines-3 lg:lines-3 text-onLight-02 md:text-onDark-02"
    )[0].getText()

    res["link"] = main_article.find_all("a", href=True)[0]["href"]

    res["intro"] = get_intro_article_page(url=res["link"])

    return res


def get_second_articles(soup):
    return soup.find_all(
        class_="w-full border-b py-2 first:border-t last:mb-2 md:first:pt-2 border-br-2-40 light:border-br-2-80"
    )


def get_second_article_infos(soup):
    res = {"title": None, "link": None}

    res["title"] = soup.find_all(
        class_="card-hover-underline font-bold -md:caps-s6-fx md-lg:caps-s6-fx lg:caps-s6-fx -md:lines-2 md-lg:lines-3 lg:lines-3 text-onLight-02"
    )[0].getText()

    res["link"] = soup.find_all("a", href=True)[0]["href"]

    res["intro"] = get_intro_article_page(url=res["link"])

    return res
