__author__ = 'Paul'
from struct import *

#Transfering data across the network transforming it to bytes
class NetworkData():

    #Store as bytes data (e.g. format of data stored as bytes: b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
    def convert_data_to_bytes(self):
        packed_data = pack("iif", 6, 19, 4.73) # iif is saying I want to store two integers and a float data types
        #print(packed_data)
        return packed_data

    #To get bytes data back to normal
    def orginal_data(self, data):
        original_data = unpack("iif", data)
        print(original_data)


x = NetworkData()
data = x.convert_data_to_bytes()
x.orginal_data(data)
x.orginal_data(b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')

# Calculating how much storage is needed to store each data type
print("Integer bytes size", calcsize("i"))
print("Floaat bytes size", calcsize("f"))
print(calcsize("iif"))
