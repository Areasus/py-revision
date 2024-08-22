# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
import os

file = open("test.txt", "rt")
# file = open("D:\\myfiles\welcome.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readline())
for line in file:
  print(line)

file.write("Now the file has more content!")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
#   os.rmdir("myfolder") #remove folder
else:
  print("The file does not exist")
