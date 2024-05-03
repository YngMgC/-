import numpy as np


class f3():
    def f3(image,binary_message):
        exitloop = False
        width,height= image.shape[:2]

        index = 0
        length = len(binary_message)
        for j in range(width // 8):
            for i in range(height // 8):
                
                for v in range(8):
                    for u in range (8):
                        a = image[i * 8 + u][j * 8 + v]
                        # 所有的字符已经全部嵌入
                        if index >= length:
                            exitloop = True
                            break

                        # 在像素矩阵中遇到0，跳过
                        if a == 0 :
                            continue  # original value is 0
                        # 在像素矩阵中遇到的不是0也不是正负1
                        elif abs(a) > 1:
                            # 如果最低位不同，绝对值减一
                            if abs(a) % 2 != int(binary_message[index]):
                                if image[i * 8 + u][j * 8 + v] < 0:
                                    image[i * 8 + u][j * 8 + v] += 1
                                    index += 1      # 右挪
                                else:
                                    image[i * 8 + u][j * 8 + v] -= 1
                                    index += 1      # 右挪
                            # 如果最低位相同，不变
                            else :
                                image[i * 8 + u][j * 8 + v] = image[i * 8 + u][j * 8 + v]
                                index += 1      # 右挪
                        # 在像素矩阵中遇到正负1
                        elif abs(a) == 1:  # original value is +/-1
                            # 如果要隐写的信息是0，则正负1置为0，跳过这一个像素
                            if binary_message[index] == '0':
                                image[i * 8 + u][j * 8 + v] = 0
                            # 如果要隐写的信息是1，则正负1不变
                            else:
                                image[i * 8 + u][j * 8 + v] = image[i * 8 + u][j * 8 + v]
                                index += 1      # 右挪
                    if exitloop:
                        break
                if exitloop:
                    break
            if exitloop:
                break
        return image
    
    def def3(image):
        index = 0
        width,height= image.shape[:2]
        message = []
        for j in range(width // 8):
            for i in range(height // 8):
                for v in range(8):
                    for u in range (8):
                        a = image[i * 8 + u][j * 8 + v]
                        # 是0，跳过，不是0则取最低位
                        if image[i * 8 + u][j * 8 + v] != 0:
                            message.append(str(abs(image[i * 8 + u][j * 8 + v]) % 2))
                            index += 1
                        # if image[i * 8 + u][j * 8 + v] == 0:
                        #     continue  # original value is 0
                        # # 不是0，也不是正负一
                        # else:
                        #     if image[i * 8 + u][j * 8 + v] % 2 == 1:
                        #         message.append('1')
                        #     elif image[i * 8 + u][j * 8 + v] % 2 == 0:
                        #         message.append('0')
                        
        return message

