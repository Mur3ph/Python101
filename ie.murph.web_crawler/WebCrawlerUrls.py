__author__ = 'Paul'
import requests
from bs4 import BeautifulSoup

class WebCrawlerFromNewBoston(object):

    def trade_spider(self, pages):
        page = 1
        while page <= pages:
            url = "https://www.thenewboston.com/forum/recent_activity.php?page=" + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser") # We put all the information from the web page into a soup object, so we can access it better
            #Get the data through the Class="" of the HTML element (..or any unique identifier)
            for link in soup.findAll("a", {"class" : "title"}):
                href = link.get("href")
                title = link.string
                #print(href)
                #print(title)
                self.get_single_item_data(href)
            page+=1

    #Take the url from last method and find url on next page
    def get_single_item_data(self, url):
        crawler_set = set()
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser") # We put all the information from the web page into a soup object, so we can access it better
        for user_name in soup.findAll("a", {"class" : "user-name"}):
            #print(link.get("href"))
            #print(user_name.string)
            crawler_set.add(user_name.string) #Put into a set, as sets don't allow duplicates

        #for link in soup.findAll("a"):
            #print(link.get("href"))

        for user in crawler_set:
            print(user)


x = WebCrawlerFromNewBoston()
x.trade_spider(1)


