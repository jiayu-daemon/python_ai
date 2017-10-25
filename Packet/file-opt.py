#!/usr/bin/python3

#!/usr/bin/python3
import os


# Open a file
#fo = open("foo.txt", "wb")
#打开一个文件只能以二进制格式写入。如果文件存在覆盖该文件。如果该文件不存在，则创建写入新文件。
fo = open("foo.txt", "w+")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.write( "Python is a great language.\nYeah its great!!\n")
# Check current position
position = fo.tell()
print ("Current file position : ", position)
# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(50)
print ("read String is : ", str)
fo.close()

# Rename a file from test1.txt to test2.txt
os.rename( "foo.txt", "test.txt" )
os.mkdir("newdir")
#os.remove("test.txt")
# Changing a directory to "/home/newdir"
os.chdir("newdir")
# This would give location of the current directory
os.getcwd()
os.mkdir("newdir")