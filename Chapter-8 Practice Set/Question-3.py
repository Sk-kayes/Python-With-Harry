def sum_n_number(num):
    if(num == 1):
        return 1
    return sum_n_number(num-1)+num

sum = sum_n_number(10)
print(sum)