# class Cookie:
#     pass

# a = Cookie()
# b = Cookie()

# print(type(a))
# print(type(b))

# class FourCal:
#     # first = 0
#     # second = 0

#     def __init__(self, first=0, second=0):
#         self.first = first
#         self.second = second

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# c=SafeFourCal(first = 2)
# print(c.div())


# a = FourCal()
# b = FourCal()

# a.setdata(4,2)
# b.setdata(3,7)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())



# c = FourCal()
# c.setdata(5, 7)
# print(c.first)
# print(c.second)
# c.first = 10
# c.second = 20
# print(c.first)
# print(c.second)

# d = FourCal()
# d.setdata(3,4)
# print(id(c.first))
# print(id(d.first))

# sumresult = c.add()
# print(sumresult)


class M:
    class_V = 0

a = M()
b = M()
print(a.class_V)
print(b.class_V)

M.class_V=5
print(a.class_V)
print(b.class_V)

a.class_V = 6
b.class_V = 10
print(a.class_V)
print(b.class_V)