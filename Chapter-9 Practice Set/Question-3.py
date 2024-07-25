# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def write_table(num):
    table = ""
    for i in range(1, 11):
        table += f"{num} X {i} = {num*i}\n"

    with open(f"13-Year Old/{num}_table.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    write_table(i)