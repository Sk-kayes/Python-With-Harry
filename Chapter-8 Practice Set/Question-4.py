def star(row): 
    if (row==0):
        return;
    print("*" * row)
    star(row-1)

star(5)