#  Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

file = open("Poem.txt", "r")
data = file.read()
idx = data.find("twinkle")
if(idx != -1):
    print("The file contains the word 'twinkle'.")
else:
    print("The file does not contain the word 'twinkle'.")

# if("twinkle" in data):
#     print("The word 'twinkle' is present in the file.")
# else:
#     print("The word 'twinkle' is not present in the file.")
file.close()