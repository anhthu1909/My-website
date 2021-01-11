# import sys
# randomList = ['a', 0, 2.0]

# for i in randomList:
#     try:
#         print("iterative:", i)
#         r = (1.0/(i))
#         break
#     except:
#         print("exception: ", sys.exc_info(),".")
#         print("Next iterative: ")
#         print()

# print("Result with iterative", i, "is:", r)

# 1
class Human:
    def __init__(self, hoten, namsinh="1999", quequan="Dong Thap", nghenghiep="Sinh vien"):
        self.hoten = hoten
        self.namsinh = namsinh
        self.quequan = quequan
        self.nghenghiep = nghenghiep

    def live(self, noicutru):
        print("{} đang sống ở {} {}".format(self.hoten, self.quequan, self.namsinh))

    def work(self, diachicoquan):
        print("{} đang làm nghề {} tai {}".format(
            self.hoten, self.nghenghiep, diachicoquan))

c = Human("Anhthu", quequan="Can Tho")
c.live("abc")
# c.work("Dai hoc Can Tho")

# 3
class Student(Human):
    def __init__(
        self, hoten, namsinh, quequan, mssv,
        nganhhoc, diemtrungbinh, nghenghiep="Student"):
        super().__init__(hoten, namsinh, quequan, nghenghiep="Student")
        self.mssv = mssv
        self.nganhhoc = nganhhoc
        self.diemtrungbinh = diemtrungbinh

    def Study(self, lop):
        print("{} co ma sinh vien {} thuoc nganh {} đang hoc tai phong {}"
            .format(self.hoten, self.mssv, self.nganhhoc, lop))

    def Rank(self):
        loai = "Yếu"
        diemtrungbinh = self.diemtrungbinh
        if(4 <= diemtrungbinh < 6):
            loai = "Trung bình"
        elif(6 <= diemtrungbinh < 8):
            loai = "Kha"
        else:
            loai = "Gioi"
        print("Sinh viên {} co mssv {} voi diem trung binh {} duoc xep loai {}".format
                (self.hoten, self.mssv, self.diemtrungbinh, loai))

# c = Student("thu", "1999", "DT", "B1704697", "HTTT", 7)
# c.Study("DI1795A2")
# c.Rank()