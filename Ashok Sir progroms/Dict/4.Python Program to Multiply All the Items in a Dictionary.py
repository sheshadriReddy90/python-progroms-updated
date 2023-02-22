dict_a={
    'a':10,
    'b':20,
    'c':30,
    'd':40
}

product=1
for val in dict_a.values():
    product=product*val
print(product)