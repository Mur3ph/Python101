__author__ = 'Paul'
import heapq
class HeapQ(object):

    def find_lardest(self, *args):
        return heapq.nlargest(3, args)


x = HeapQ()

grades = [34, 66, 87, 18, 76, 95, 44, 53, 100, 11]
largest = x.find_lardest(grades)
print(largest)
print(heapq.nlargest(3, grades))

stocks = [
    {"Company": "GOOG", "Price": 520.54},
    {"Company": "FB", "Price": 76.45},
     {"Company": "YHOO", "Price": 39.28},
    {"Company": "AMZN", "Price": 306.21},
    {"Company": "AAPL", "Price": 99.76}
]

print(heapq.nsmallest(3, stocks, key=lambda stock: stock["Price"]))
