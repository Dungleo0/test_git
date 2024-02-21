from math import *


class Phanso:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau

    def get_tu(self):
        return self.__tu

    def set_tu(self, tu):
        self.__tu = tu

    def get_mau(self):
        return self.__mau

    def set_mau(self, mau):
        self.__mau = mau

    def toi_gian(self):
        ucln = gcd(self.__tu, self.__mau)
        self.__tu //= ucln
        self.__mau //= ucln

    def __str__(self):
        return f"{self.__tu}/{self.__mau}"


class Main:
    if __name__ == '__main__':
        print("nhap tu va mau cua phan so: ")
        tu, mau = map(int, input().split())
        p = Phanso(tu, mau)
        p.toi_gian()
        print(p)
