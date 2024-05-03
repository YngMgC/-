import numpy as np
import cv2
class dct_quant():
    def lianghua(dct_img):
        # 亮度量化表
        quant_tbl_liangdu = np.array(  # quantify table
            [
                [16, 11, 10, 16, 24, 40, 51, 61],
                [12, 12, 14, 19, 26, 58, 60, 55],
                [14, 13, 16, 24, 40, 57, 69, 56],
                [14, 17, 22, 29, 51, 87, 80, 62],
                [18, 22, 37, 56, 68, 109, 103, 77],
                [24, 35, 55, 64, 81, 104, 113, 92],
                [49, 64, 78, 87, 103, 121, 120, 101],
                [72, 92, 95, 98, 112, 100, 103, 99],
            ]
        )

        # 色差量化表
        quant_tbl_secha = np.array(
            [
                [17, 18, 24, 47, 99, 99, 99, 99],
                [18, 21, 26, 66, 99, 99, 99, 99],
                [24, 26, 56, 99, 99, 99, 99, 99],
                [47, 66, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
                [99, 99, 99, 99, 99, 99, 99, 99],
            ]
        )

        width, height = dct_img.shape[:2]

        quant_blocks = []       # 存储量化后的矩阵
        for i in range(3):
            # 将DCT图像分割成8x8大小的块。
            # 使用np.vsplit()将DCT图像的高度分割成多个8像素的块，
            # 使用np.hsplit()将每个块的宽度分割成多个8像素的块。
            # 得到的img_blocks是一个二维列表，其中每个元素代表一个8x8的图像块。
            img_blocks = [
                np.hsplit(item, width // 8)
                for item in np.vsplit(dct_img[:, :, i], height // 8)
            ]
            dct_blocks = [
                [np.array(cv2.dct(block), dtype=int) for block in line]
                for line in img_blocks
            ]
            # 根据颜色通道选择相应的量化表。对于红色通道（i == 0），使用quant_tbl_1作为量化表；对于绿色和蓝色通道，使用quant_tbl_2作为量化表。
            quant_tbl = quant_tbl_liangdu if i == 0 else quant_tbl_secha
            # 对DCT系数进行量化。
            # 将DCT系数除以相应的量化表，使用整数类型（dtype=int）保存结果，
            # 并将它们存储在quant_blocks列表中。
            quant_blocks.append(
                [
                    [np.array(item / quant_tbl, dtype=int) for item in line]
                    for line in dct_blocks
                ]
            )
        return quant_blocks