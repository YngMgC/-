class text():
    def change(path):
        binary_sequence = []

        with open(path, "r") as file:
            content = file.read()
            for char in content:
                binary = bin(ord(char))[2:].zfill(8)  # 将字符转换为8位的二进制序列
                binary_sequence.append(binary)

        # print(binary_sequence)
        return binary_sequence
    
    def change_back(binary_string,length):
        text = ""
        start_index = 16
        hidden_message = binary_string[start_index:start_index+length]
        message = "".join(hidden_message)
        return message
        # # for binary in hidden_message:
        # #     decimal = int(binary, 2)
        # #     char = chr(decimal)
        # #     text += char
        # # 将二进制串按照八位一组分割
        # binary_list = [message[i:i+8] for i in range(0, len(message), 8)]

        
        
        # # 假设有一个名为output_file的文件对象，用于写入识别结果
        # output_file = open("reader.txt", "w")

        # # 将识别的字符串写入文件
        # output_file.write(chinese_text)

        # # 关闭文件
        # output_file.close()