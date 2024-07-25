def max_num(a, b, c):
    if (a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
        
max = max_num(9,4,3)
print(max)