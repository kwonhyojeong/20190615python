# def add(a,b):
#     result = a + b
#     print("a = ",a)
#     print("b = ",b)
#     return result

# print(add(4,5))


# def add(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(add(1,3,5,7,9))


# def print_kwargs(**args):
#     print(args)

# print_kwargs(name = 'kang', age = 33, city = 'busan')


a = 1
def test_1():
    global a
    a += 1
    

test_1()
print(a)