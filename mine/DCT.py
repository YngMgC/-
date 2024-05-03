''' 对图像做DCT变换,得到DCT系数 '''
import cv2
import numpy as np

class DCT():
    # 分块图 DCT 变换
    def block_img_dct(img_f32):
        height, width = img_f32.shape[:2]
        # 将高度和宽度除以8来确定垂直和水平方向上的块数
        block_y = height // 8
        block_x = width // 8
        # 确保图像可以被块均匀地分割
        height_ = block_y * 8
        width_ = block_x * 8
        img_f32_cut = img_f32[:height_, :width_]
        img_dct = np.zeros((height_, width_), dtype=np.float32)     # 存储DCT系数


        # 从img_f32_cut中提取一个大小为8x8的块，并使用cv2.dct()应用DCT变换
        for h in range(block_y):
            for w in range(block_x):
                # 对图像块进行dct变换
                img_block = img_f32_cut[8*h: 8*(h+1), 8*w: 8*(w+1)]
                img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)] = cv2.dct(img_block)
        return img_dct
    
    def block_img_idct(img_dct):
        new_img = img_dct.copy()        # 存储重建的图像
        height, width = img_dct.shape[:2]
        # 将高度和宽度除以8来确定垂直和水平方向上的块数
        block_y = height // 8
        block_x = width // 8
        for h in range(block_y):
            for w in range(block_x):
                # 进行 idct 反变换
                dct_block = img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)]
                img_block = cv2.idct(dct_block)
                new_img[8*h: 8*(h+1), 8*w: 8*(w+1)] = img_block
        return new_img


    



