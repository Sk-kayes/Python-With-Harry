# Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if "python" in line:
        print(f"Python is present in the line: {lineno}")
        break
    lineno += 1
else:
    print("Python is not present in the file.")