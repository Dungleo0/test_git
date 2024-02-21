# print('hello world')
# age = 18
# print('toi dang' , age)
# nhap du lieu
# a,b,c,d = map(int,input("nhap vao day du so: ").split())
# print(a,b,c,d)
# in chu so cuoi cung

# number = 1005

# end_digit = number % 10

# print(f"{end_digit}".format(end_digit))
# print(number % 100)

# phep chia
# a = 10
# b = 3
# print(a//b)
# print(a/b)
# print("%.2f" %(a/b))

# xoa so
# n = 123456
# print(n // 1000)

# tinh toan
# import math
#
# x = int(input("nhap gia tri can tinh: "))
# A = x**2 + 2*x + 1
# print(A)

# cau lenh re nhanh

# n = int(input("nhap so nguyen duong: "))

# if(n % 2 == 0):
#     print("YES")
# else:
#     print("NO")
#
# if(n % 3 == 0 and n % 5 == 0):
#     print("YES")
# else:
#     print("NO")
#
# if(n % 3 == 0 and n % 7 != 0):
#     print("YES")
# else:
#     print("NO")
#
# if(n % 3 == 0 or n % 7 == 0):
#     print("YES")
# else:
#     print("NO")
#
# if(n > 30 and n < 70):
#     print("YES")
# else:
#     print("NO")

# cho a,b tim 2 so: so 1 lon nhat <= a % b ==0 , so 2 min >= a % b ==0, khong dung vong lap
# a, b = map(int, input("nhap 2 so: ").split())
# num = [x for x in range(a) if x < a and x % b ==0]
# print(max(num))

# ktra nam nhuan
# n = int(input("nhap nam: "))
# if(n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
#     print("YES")
# else:
#     print("NO")

# tam giac hop le
# a, b, c = map(int, input("nhap a,b,c: ").split())
# if (a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b):
#     if (a == b == c):
#         print("Tam giac deu")
#     elif (a == b or a == c or b == c):
#         print("Tam giac can")
#     elif (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2):
#         print("Tam giac vuong")
#     else:
#         print("Tam giac thuong")
# else:
#     print("Ko la Tam giac")

# red_flag = True
# y, m = map(int, input("nhap nam, thang: ").split())
# if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
#     red_flag = False
#
# if (m <= 12 and m >= 1):
#     if(m in [1, 3, 5, 7, 8, 10, 12]):
#         print("thang", m, "nam", y, "co 31 ngay")
#     elif (m == 2):
#         if (red_flag):
#             print("thang 2 co 28 ngay")
#         else:
#             print("thang 2 cos 29 ngay")
#     elif (m in [4, 6, 9, 11]):
#         print("thang", m, "nam", y, "co 30 ngay")
# else:
#     print("nhap sai dinh dang thang, nam")

# doi ngay sang nam tuan ngay biet 1 nam co 365 ngay

# n = int(input("day: "))
# nam = n // 365
# n = n % 365
# tuan = n // 7
# n = n % 7
# print(nam, tuan, n)

# doi giay sang gio,phut,giay
# n = 4321
# h = n // 3600
# n = n % 3600
# m = n // 60
# n = n % 60
# s = n % 60
# print(h, m, s)

# tinh diem
# a, b, c, d = map(float, input("nhap 4 diem: ").split())
# result = (a + b + 2 * c + 3 * d) / 7.0
# if (result >= 8):
#     print("GIOI")
# elif (result < 8 and result >= 6.5):
#     print("KHA")
# elif (result <= 6.5 and result > 5):
#     print("TB")
# elif (result < 5):
#     print("YEU")

# chuyen ki tu tiep theo trong bang chu cai
# c = input()
# if (c == 'z' or c== 'Z'):
#     print("a")
# else:
#     tmp = ord(c)
#     tmp = tmp + 1
#     print(chr(tmp).lower())

# kiem tra ki tu in hoa, thuong, hay ki tu dac biet
# c = input()
# print(c.isalnum())

# tong cac uoc

# from math import *
#
# n = 16
# tong = 0
# for i in range(1,isqrt(n)+1):
#     if n % i == 0:
#         tong += i
#         if i != n // i:
#             tong += n // i
# print(tong)

# in so chinh phuong
# from math import *
#
# dem = 0
# n = int(input())
#
# for i in range(1, isqrt(n) + 1):
#     print(i * i, end=" ")
#     dem += 1
# print()
# print(dem)

# tich cac uoc

# from math import *

# n = int(input())
# tich = 1
# for i in range(1,n+1):
#     if n % i == 0:
#         tich *= i
#         print(i)
# print(tich)

# def tn(n):
#     temp = n
#     res = 0
#     while n > 0:
#         res = res * 10 + n % 10
#         n //= 10
#     return temp == res
#
# def check(n):
#     last = n % 10
#     m = 0
#     while n >= 10:
#         m = m * 10 + n % 10
#         n //= 10
#     return ( (last * 2 == n) or(n * 2 == last)) and tn(m)
#
# if __name__ == '__main__':
#     n = int(input())
#     if(check(n)):
#         print("YES")
#     else:
#         print("NO")
# from math import *
# def check(n):
#     sum = 0
#     for i in range(2, isqrt(n)):
#         if(n > 0):
#             print(n,end=" ")
#
# if __name__ == '__main__':
#     n = int(input())
#     check(n)
#
# def check(n, k):
#     count = 0
#     for i in range(2, n):
#         if (n % i == 0):
#             while (n % i == 0):
#                 count += 1
#                 n //= i
#                 if count == k:
#                     print(i)
#     if count < k or k <= 0:
#         print("-1")
#
#
# if __name__ == '__main__':
#     n, k = map(int,input().split())
#     check(n, k)

# 18 = 2 * 3**2

# def check(n):
#     for i in range(2,n):
#         if (n % i == 0):
#             mu =0
#             while(n % i == 0):
#                 mu+=1
#                 n//=i
#             print(i,"^",mu,"*",end=" ")
#
# if __name__ == '__main__':
#     n = int(input())
#     check(n)
#
# # tan suat
# def check():
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = [0] * 10000000
#     for i in a:
#         b[i] += 1
#     for i in a:
#         if b[i] != 0:
#             print(b[i], i)
#             b[i] = 0

# if __name__ == '__main__':
#     check()
#

# a = [1, 3, 5, 2, 4, 5, 6, 4]
# cnt = [0] * 100000
# for i in a:
#     cnt[i] = 1
# dem = 0
# for i in a:
#     if cnt[i] != 0:
#         dem += 1
#         cnt[i] = 0
#         print(i,end=" ")

# khoang cach giua 2 cap nho nhat
# a = [1, 3, 5, 2, 4, 5, 6, 4]
# k = 100000
# for i in range(0, len(a)):
#     for j in range(i + 1, len(a) - 1):
#         if abs(a[i] - a[j]) < k:
#             k = abs(a[i] - a[j])
#
# print(k)

# liet ke cac gia tri xuat hien trong mang
# c1
# a = [1, 2, 5, 2, 6, 7, 3, 5, 0]
# b = []
# for i in range(0, len(a)):
#     if a[i] not in b:
#         b.extend([a[i]])
# print(b)
# # c2 su dung mang danh giau
# c = [0] * 1000000
# for i in a:
#     if c[i]==0:
#         print(i,end=" ")
#         c[i] = 1
# # c2 su dung for truoc do
# print()
# for i in range(len(a)):
#     check = False
#     for j in range(0,i):
#         if a[i] == a[j]:
#             check = True
#             break
#     if not check:
#         print(a[i],end=" ")
#
# in ra chi so i neu tong gia tri ben trai i la 1 snt va tong gia tri ben phai la 1 snt
# from math import *
#
#
# def nt(n):
#     if n < 2:
#         return False
#     for i in range(2, isqrt(n)+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# a = [53, 5, 69, 47, 19]
# for i in range(0, len(a)):
#     left = 0
#     for j in range(0, i):
#         left += a[j]
#     right = 0
#     for j in range(i + 1, len(a)):
#         right += a[j]
#     if nt(right) and nt(left):
#         print(i, end=" ")
# a = [1, 5, 2, 5, 6, 3, 5, 7, 4]
# max1 = a[0]
# max2 = a[0]
# for i in a:
#     if i > max1:
#         max1 = i
#     elif i > max2:
#         max2 = i
# print(max1, max2)
# ngay_sinh = "1/2/2004"
# if ngay_sinh[1] == '/':
#     ngay_sinh = '0' + ngay_sinh
# if ngay_sinh[4] == '/':
#     ngay_sinh = ngay_sinh[0:3] + '0' + ngay_sinh[3:]
# print(ngay_sinh, end=" ")
# ten = "   dInh    QuANG dUNG"
# ten = ten.split()
# ten = " ".join(ten)
# ten = ten.title()
# print(ten)
# a = [1, 2, 4, 2, 4, 5, 6, 0]
# a.sort(key=lambda x: -x)
# print(a)
