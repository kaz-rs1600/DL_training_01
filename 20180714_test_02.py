def test(a, b):
    return a + b

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = test(list_a, list_b)
print("list_a:{0}".format(list_a))
print("list_b:{0}".format(list_b))
print("list_c:{0}".format(list_c))
