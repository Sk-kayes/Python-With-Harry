letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter name: ")
date = input("Enter date: ")

updated_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
print(updated_letter)
