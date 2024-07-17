#1
# given_list = [5, 4, 3, 2, 2, 1, 0, -1, -2, ]
# total = 0
# i = 0
# while i<len(given_list):
#     if given_list[i] < 0:
#         total += given_list[i]
#         i = i + 1
#     else:
#         i = i+1
# print(total)

#2
# given_list2 = [5, 4, 3, 2, 2, 1, 0, -1, -2, ]
# total2 = 0
# for element in given_list2:
#     if element <= 0:
#         total2 += element
# print(total2)

#3
# class Robot:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#
#     def introduce_self(self):
#         print("My name is " + self.name)
#
#
# # r1.name = "Tom"
# # r1.color = "red"
# # r1.weight = 30
# # r2 = Robot()
# # r2.name = "Jerry"
# # r2.color = "blue"
# # r2.weight = 40
# r1 = Robot("Tom", "red", 30)
# r2 = Robot("Jerry", "blue", 40)
# r1.introduce_self()
# print(r2.name)

# a = [1, 3, 5, 6, 11, 3]
# b = []
# b.append(2 * a)
# print(b)

a = [1, 3, 5, 6, 11, 3]
b = []
for m in a:
    b.append(2 * m)
print(b)
c = [x*x for x in a]
print(c)