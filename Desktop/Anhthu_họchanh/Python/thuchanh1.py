print("Welcome to Python")

# 2
# print("Nhap ho ten:")
# hoten = input()
# print("Hello " + hoten + "," + " Welcome to Python")
# 3

# print("Nhap a:")
# a = int(input())
# print("Nhap b")
# b = int(input())
# if b == 0:
#     print('Nhap lai b:')
#     b = int(input())
# else:
#     print ("a + b = ",a + b)
#     print ("a - b = ",a - b)
#     print ("a * b = ",a * b)
#     print ("a / b = ",a / b)
#     print ("a % b = ",a % b)
#     print ("a ** b = ",a ** b)
# 4
# print("Nhap r:")
# r = int(input())
# print("Chu vi hinh tron = ", 2*r*3.14)
# print("Dien tich hinh tron = ", r*r*3.14)

# 5
# print("Nhap n:")
# n = int(input())
# if n < 0:
#     print("Vui long nhap lai n:")
#     n = int(input())
# else:
#     s = 1
#     for i in range(1, n+1):
#         s = s * i
#     print("n! = ", s)

# # 6
# import math

# print("Nhap a:")
# a = int(input())
# print("Nhap b:")
# b = int(input())
# print("Nhap c:")
# c = int(input())
# delta = b * b - 4 * a * c
# if a == 0:
#     print("Giai phuong trinh bac 1")
# else:
#     if delta < 0:
#         print("Phuong trinh vo nghiem")
#     elif delta == 0:
#         print("Phuong trinh co nghiem kep: x1=x2=", -b/2*a)
#     else:
#         print("Phuong trinh co 2 nghiem phan biet:")
#         print("x1=", (-b + math.sqrt(delta))/2*a)
#         print("x2=", (-b - math.sqrt(delta))/2*a)

# 7
# for i in range(5000, 7000):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)

# 10
# import math
# print("Nhap n:")
# n = int(input())
# for i in range(2, n):
#     s = 0
#     for j in range(2, math.ceil(i/2)+1):
#         if i % j == 0:
#             s+=1
#     if(s == 0):
#         print(i)
# 11
import math

def nhapso(min, max):
    # print("So bat dau:")
    # min = int(input())
    # print("So ket thuc:")
    # max = int(input())
    for i in range(min, max):
        s = 0
        for j in range(2, math.ceil(i/2) + 1):
            if i % j == 0:
                s+=1
        if(s == 0):
            print(i)

# nhapso(1000,9999)

# 12
# print("nhap n:")
# n = input()
# if int(n) < 0:
#     print("Nhap lai n:")
#     n = input()
# else:
#     s = 0
#     for i in range(0, len(n)):
#         s = s + int(n[i])
#     print("Tong gia tri chuoi = ",s)

def tongchuoi(n):
    s = 0
    for i in range(0, len(n)):
        s = s + int(n[i])
    return s

# print(tongchuoi("456"))

# 15
def  f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n-1) + f(n-2)
# print(f(1))
