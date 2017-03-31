# from urllib import request as rq
from bs4 import BeautifulSoup as bfs
import requests as rq


bseNoticePage = "http://www.bseindia.com/markets/MarketInfo/NoticesNCirculars.aspx?expandable=0"
try:
    page = rq.get(bseNoticePage)
    soup = bfs(page.text, "html.parser")
    print(soup.prettify())
    # aTags = .find('a',{ 'class' : 'tablebluelink')
    # soup.find( class = "tablebluelink")
    # print(aTags)
    # print(soup.a['class'])
except Exception as ex:
    ex.__traceback__()

