# Write a program to mine a log file and find out whether it contains ‘python’

with open("log.txt", "r") as f:
    word = f.read()

if "python" in word:
    print("Python is present in the file.")
else:
    print("Python is not present in the file.")
