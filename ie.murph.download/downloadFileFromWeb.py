__author__ = 'Paul'

from urllib import request

class DownloadFile(object):

    #Get other types of data at Yahoo: http://finance.yahoo.com/
    google_historical_finance_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=0&e=26&f=2016&g=d&a=2&b=27&c=2014&ignore=.csv"
    def download_google_stock_data(self, csv_url):
        responce = request.urlopen(csv_url)
        csv_file = responce.read()
        csv_string = str(csv_file)                  #Because I don't know what format the data is I convert to string
        lines = csv_string.split("\\n")
        return lines


    def write_data_to_file(self, data):
        destination_url_data = r"google_finances.txt"   #r stands for raw, which allows you to build a url path without having to escape characters
        file_write = open(destination_url_data, "w")
        for line in data:
            file_write.write(line + "\n")
        file_write.close()

    def read_data_from_file(self):
         destination_url_data = r"google_finances"   #r stands for raw, which allows you to build a url path without having to escape characters
         file_read = open(destination_url_data, "r")
         for line in file_read:
            file_read.write(line, "\n")
         file_read.close()


x = DownloadFile()
lines = x.download_google_stock_data(x.google_historical_finance_url)
x.write_data_to_file(lines)

