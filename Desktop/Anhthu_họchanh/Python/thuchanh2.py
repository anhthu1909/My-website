# print('abc')
# # 1
# # print('a' in "abc")


# def chuoi(a):
#     s1 = 0
#     s2 = 0
#     for i in range(0, len(a)):
#         if a[i] in "0123456789":
#             s1 += 1
#         else:
#             s2 += 1
#     s3 = []
#     s3.append(s1)
#     s3.append(s2)
#     return s3


# c = chuoi("Anhthu1909")
# print(c[1])
# 2


# def chuoi(a):
#     s1 = 0
#     s2 = 0
#     for i in range(0, len(a)):
#         if a[i].isalpha():
#             if a[i].upper() == a[i]:
#                 s1 += 1
#             else:
#                 s2 += 1
#     s3 = {}
#     s3[1] = s1
#     s3[5] = s2
#     return s3


# print(chuoi("AnhThu1909"))


# 3
# def chuoi(a):
#     s1 = a.upper()
#     return s1


# print(chuoi("AnhThu1909"))

# 4
# s = []
# s1 = " - ";
# for i in range(100, 300):
#     if i % 2 == 0:
#         s.append(str(i))

# print(s1.join(s))

# 5
# print("Nhap chuoi:")
# s = input()
# s1 = s.split(',')
# s2 = []
# for i in range(0, len(s1)):
#     if s1[i].isdigit():
#         if int(s1[i]) % 2 != 0:
#             s2.append(s1[i])
# print(s2)

# 6
# s = {}
# for i in range(1, 20+1):
#     s[i] = i * i
#     print(i, "-", s[i])

# # 7
# s = [12,24,35,70,88,120,155]
# # s.remove(12)
# # s.remove(120)
# # s.remove(88)
# # print(s)
# s.pop(0)
# a = s.pop(4)
# print(a)
# print(s)

# # 9
# s = []
# for i in range(1, 20+1):
#     s.append(i*i)
# for j in range(5, len(s)):
#     print(s[j])

# 11
# s = input()
# s1 = {}
# for i in range(0, len(s)):
#     s1[s[i]] = s.count(s[i])
# for x in s1:
#     print(x, ":", s1[x])

# 12
# s = input()
# s1 = []
# s2 = ""
# for i in range(0, len(s)):
#     s1 += s[len(s) - 1 - i]
# print(s2.join(s1))

# 13 (1)
# s = input()
# s1 = ""
# # s1 = s1 + s[0] + s[1] + s[len(s) - 2] + s[len(s) - 1]
# s1 = s[0:2] + s[len(s)-2:]
# print (s1)

# 14
# print("Nhap chuoi 1:")
# s1 = input()
# print("Nhap chuoi 2:")
# s2 = input()
# s3 = s2[0:2] + s1[2:] + " " + s1[0:2] + s2[2:]
# print (s3)

# 15
s = input()
temp = s[0]
for i in range(2, len(s)):
    if(s[0] == s[i]):
        s = s.replace(s[i], "@")
        s = temp + s[1:]
print (s)