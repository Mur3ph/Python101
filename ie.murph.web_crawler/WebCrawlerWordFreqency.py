__author__ = 'Paul'
import requests
from bs4 import BeautifulSoup
import operator

class WordFrequency(object):

    def start(self, url):
        word_list = []
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser") # We put all the information from the web page into a soup object, so we can access it better
        #Get the data through the Class="title" of the HTML element (..or any unique identifier)
        for link in soup.findAll("a", {"class" : "title"}):
            href = link.get("href")
            title = link.string
            words = title.lower().split()
            for each_word in words:
                #print(each_word)
                word_list.append(each_word)
        self.clean_up_list(word_list)


    def  clean_up_list(self, word_list):
        clean_word_list = []
        for word in word_list:
            symbols = "!\"$%^&*()_+{}:@~<>?|-=[];'#,.\/" # Adding the English money sign seems to break it
            for i in range(0, len(symbols)):
                word = word.replace(symbols[i], "") #Replace symbol with blank space ""
            if len(word) > 0:   #We don't want to print empty spaces, if we replace two symbols beside each other
                #print(word)
                clean_word_list.append(word)
        self.create_dictionary(clean_word_list)


    def create_dictionary(self, clean_word_list):
        word_count_dictionary = {}
        for word in clean_word_list:
            if word in word_count_dictionary:
                word_count_dictionary[word] += 1
            else:
                 word_count_dictionary[word] = 1
        for key,value in sorted(word_count_dictionary.items(), key=operator.itemgetter(1)): # 1 is sorting by value and 0 would sort by key
            print(key, value)




#"https://www.thenewboston.com/forum/recent_activity.php?page=1"
x = WordFrequency()
x.start("https://www.thenewboston.com/forum/recent_activity.php?page=1")

