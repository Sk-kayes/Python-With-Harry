# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "fool", "bad"]
with open("new-poem.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))
with open("new-poem.txt", "w") as f:
    f.write(content)