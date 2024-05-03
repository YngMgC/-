import cv2
import numpy as np
from DCT import DCT
from quant_gray import quant,dequant
from text import text
from f3 import f3

def compare_strings(str1, str2):
    if str1 == str2:
        return "字符串相等"
    else:
        return "字符串不相等"
    

read_img_path = 'juzhen.png'
read_image = cv2.imread(read_img_path,0)
if read_image is None:
    raise Exception("Image is not found")

# # 将彩色图像转换为灰度图像
# read_image = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)


# height, width = read_image.shape[:2]
# # 将高度和宽度除以8来确定垂直和水平方向上的块数
# block_y = height // 8 
# block_x = width // 8 
# # 确保图像可以被块均匀地分割
# new_height = block_y * 8
# new_width = block_x * 8
# new_img = np.zeros((new_height, new_width), dtype=read_image.dtype)
# new_img = read_image[:new_height, :new_width]

secret = f3.def3(read_image)
# 分割字符串并提取前16位信息
first_16 = secret[:16]
first_16 = "".join(first_16)
# dct_img = DCT.block_img_dct(new_img)
# processed_image = quant(dct_img)
# processed_image = processed_image.astype(np.int8)
length = int(first_16, 2)

secret = text.change_back(secret,length)

text_path = '1.txt'
message = text.change(text_path)
binary_string = "".join(message)
compare_strings(binary_string,secret)



# secret = "".join(secret)
# print(secret)
