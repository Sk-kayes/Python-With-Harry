def st_li(li, word):
    new_li = []
    for item in li:
        if not (item == word):
            new_li.append(item.strip(word))
    return new_li


list = ["kayes", "iAlbi", "Mousin", "Nishat", "Ansari", "bi"]
new_list = st_li(list, "bi")
print(new_list)
