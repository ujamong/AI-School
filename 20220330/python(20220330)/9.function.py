def sum(left, right):
    return left+right

print(sum(10,20))


#실습
def discount(price, percent):
    percent = percent/100
    return price*(1 - percent)

print(discount(10000, 10))