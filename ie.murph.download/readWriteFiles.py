__author__ = 'Paul'

class ReadWrite(object):

     #Create a file and write to it
    def create_file_write_to_it(self):
         file_write = open("sample.txt", "w")
         file_write.write("Writing some stuff in my first file\n")
         file_write.write("Writing some stuff on the second line\n")
         file_write.close() #Frees up memory

    def read_from_file(self):
        file_read = open("sample.txt", "r")
        text = file_read.read()
        print("Read", text)
        file_read.close()

x = ReadWrite()
x.create_file_write_to_it()
x.read_from_file()

