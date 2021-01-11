# ## Phan 1
# 1
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
# print(np.array([1, 3]))
# 2
# print(np.array([1, 2, 3], [4, 5, 6]))
# 3
# arr = np.zeros(10, np.int8)
# arr[5] = 13
# print (arr)

# 4
# arr = np.zeros([5,5], np.int8)
# arr[0] = np.ones([1], np.int8)
# arr[4] = np.ones([1], np.int8)
# arr[:, 0] = np.ones([1], np.int8)
# arr[:, 4] = np.ones([1], np.int8)
# print(arr)

# 5
# arr = np.ones([3,3], np.int8)
# arr = np.pad(arr, (2,1), 'constant', constant_values=(3, 0))
# print(arr)

# 6
# arr = np.array([[10, 20, 40, 60, 70], [10, 30, 50, 60]], dtype=object)
# arr1 = np.intersect1d(arr[0], arr[1])
# print(arr1)

# 7
# print(np.linspace(2,100, 50))

# ##Phan 2
# x = [1, 2, 3, 5, 8, 6, 4]

# plt.plot(x)
# plt.show()

# 8
# x = np.linspace(-10, 10, 100)
# y = np.sin(x)

# plt.scatter(x, y)
# plt.show()

# 9
# x = np.linspace(-5, 5, 20)
# y = x ** 3 - 2 * x ** 2 + x + 5
# plt.scatter(x, y)
# plt.plot(x, y)
# plt.show()

# 10
# x = np.linspace(-10, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label = 'sin(x)')
# plt.plot(x, y2, label = 'cos(x)')

# plt.title('Đồ thi hinh sin va cos')
# plt.legend()

# plt.show()

# 11
# x1 = np.linspace (-10, 10, 100)
# x2 = np.linspace (-1.5, 1.5, 100)
# y1 = np.sin(x1)
# y2 = np.cos(x1)
# y3 = np.tan(x2)

# ax1 = plt.subplot(1, 3, 1)
# ax1.set_xlim([-2, 2])
# ax1.set_ylim([-2, 2])
# plt.plot(x1, y1, 'red', label = 'sin(x1)')

# ax2 = plt.subplot(1, 3, 2)
# plt.plot(x1, y2,'green' , label = 'cos(x1)')
# ax2.set_xlim([-2, 2])
# ax2.set_ylim([-2, 2])

# ax3 = plt.subplot(1, 3, 3)
# plt.plot(x2, y3,'blue' , label = 'tan(x2)')
# ax3.set_xlim([-2, 2])
# ax3.set_ylim([-2, 2])

# plt.show()

# ##Phan 3

from PIL import Image
# 12
# im = Image.open("094455_6.jpg")
# im.show()

# 14
# im = Image.open("094455_6.jpg")
# im_180 = im.rotate(180)
# im_180.save("anhchinhsua.jpg")
# im_180.show()

# 15
# im = Image.open("094455_6.jpg")
# im_cvt = im.convert('1')
# im_90 = im_cvt.rotate(90)
# im_90.save("anhtrangden.jpg")
# im_90.show()