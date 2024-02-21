class Student:
    def __init__(self, name, date, point):
        self.__name = name
        self.__date = date
        self.__point = point

    def __str__(self):
        return f"name: {self.__name}\ndate: {self.__date}\npoint: {self.__point}"


class Main:
    if __name__ == '__main__':
        print("nhap ten, ngay sinh, tong diem: ")
        name, date, point = map(str, input().split())
        s = Student(name, date, point)
        print(s)
