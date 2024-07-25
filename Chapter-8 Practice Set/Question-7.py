def table(num, mul=1, limit=11):
    if (mul == limit):
        return num*mul
    else:
        print(num*mul)
        table(num, mul+1)


table(5)
