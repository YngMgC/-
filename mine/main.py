import cv2
import numpy as np
from DCT import DCT
from quant_gray import quant,dequant
from text import text
from f3 import f3

# 读入图像
img_path = 'R.jpg'
img = cv2.imread(img_path)
if img is None:
    raise Exception("Image is not found")

# 读入隐藏信息的文件
text_path = '1.txt'

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

yuv_image = gray_image.astype(np.float32)

height, width = yuv_image.shape[:2]
# 将高度和宽度除以8来确定垂直和水平方向上的块数
block_y = height // 8 
block_x = width // 8 
# 确保图像可以被块均匀地分割
new_height = block_y * 8
new_width = block_x * 8
new_img = np.zeros((new_height, new_width), dtype=yuv_image.dtype)
new_img = yuv_image[:new_height, :new_width]

# DCT变换
dct_img = DCT.block_img_dct(new_img)
# cv2.imwrite("dct.jpg", dct_img)

# 量化
processed_image = quant(dct_img)
# cv2.imwrite("quant.jpg", processed_image)
# print(processed_image)

# 在文件的头16bit加入长度信息
message = text.change(text_path)
binary_string = "".join(message)
length = len(binary_string)
length_string = bin(length)[2:]  # 使用 bin() 函数将整数转换为二进制字符串，并去掉前缀 '0b'
if len(length_string) < 16:
    length_string = "0" * (16 - len(length_string)) + length_string
result_string = length_string + binary_string

# binary_string = text.change_back(message)
# print('原来',binary_string)

# 完成隐写
processed_image = processed_image.astype(np.int8)
hidden_image = f3.f3(binary_message = result_string,image = processed_image)
# cv2.imwrite("hidden_image.jpg", hidden_image)

# secret = f3.def3(hidden_image)
# secret = "".join(secret)
# print('提取hidden',secret)

# np.save('array.npy', hidden_image)
cv2.imwrite("juzhen.bmp", hidden_image)


def show(jpeg):
    dequan_img = dequant(jpeg)
    dedct_img = DCT.block_img_idct(dequan_img)
    # cv2.imshow('Image', dedct_img)
    cv2.imwrite("jiami.jpg", dedct_img)
    
show(hidden_image)

secret = f3.def3(hidden_image)
# 分割字符串并提取前16位信息
first_16 = secret[:16]
first_16 = "".join(first_16)
# dct_img = DCT.block_img_dct(new_img)
# processed_image = quant(dct_img)
# processed_image = processed_image.astype(np.int8)
length = int(first_16, 2)

secret = text.change_back(secret,length)

def compare_strings(str1, str2):
    if str1 == str2:
        print("字符串相等") 
    else:
        print("字符串不相等")

text_path = '1.txt'
message = text.change(text_path)
binary_string = "".join(message)
compare_strings(binary_string,secret)







