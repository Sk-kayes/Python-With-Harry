# Write a program to find out whether a file is identical & matches the content of 
# another file.

with open("this.txt", "r") as f:
    content_1 = f.read()

with open("poem.txt", "r") as f:
    content_2 = f.read()

if(content_1 == content_2):
    print("Content is identical")
else:
    print("Content is not identical")