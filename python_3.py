numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def filter_even_num(i):
    if(i % 2) == 1 and i >= 50:
        return True
    else:
        return False
f = filter(filter_even_num, numbers)
print(list(f))
