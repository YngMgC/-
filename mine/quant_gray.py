import numpy as np
import cv2
def quant(dct_img):
    quantization_matrix = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ])

    height, width = dct_img.shape[:2]
    # 将高度和宽度除以8来确定垂直和水平方向上的块数
    block_y = height // 8
    block_x = width // 8
    # 确保图像可以被块均匀地分割
    height_ = block_y * 8
    width_ = block_x * 8
    img_f32_cut = dct_img[:height_ , :width_]
    img_quant = np.zeros((height_, width_), dtype=np.float32) 
    # 从img_f32_cut中提取一个大小为8x8的块，并使用cv2.dct()应用DCT变换
    for h in range(block_y):
        for w in range(block_x):
            # 对图像块进行dct变换
            img_block = img_f32_cut[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_quant[8*h: 8*(h+1), 8*w : 8*(w+1) ] = img_block / quantization_matrix
    return img_quant   # 存储DCT系数

def dequant(hidden_img):
    quantization_matrix = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ])

    height, width = hidden_img.shape[:2]
    # 将高度和宽度除以8来确定垂直和水平方向上的块数
    block_y = height // 8
    block_x = width // 8
    # 确保图像可以被块均匀地分割
    height_ = block_y * 8
    width_ = block_x * 8
    img_f32_cut = hidden_img[:height_ , :width_]
    img_quant = np.zeros((height_, width_), dtype=np.float32) 
    # 从img_f32_cut中提取一个大小为8x8的块，并使用cv2.dct()应用DCT变换
    for h in range(block_y):
        for w in range(block_x):
            # 对图像块进行dct变换
            img_block = img_f32_cut[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_quant[8*h : 8*(h+1) , 8*w : 8*(w+1)] = img_block * quantization_matrix
    return img_quant   # 存储DCT系数