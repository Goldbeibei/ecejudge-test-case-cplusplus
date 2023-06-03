# -*- coding: utf-8 -*-

# 使用者設定--------------------------------------------
# 中文測資輸出(預設為True)
no_zh_output = True


# ----------------------------------------------------

import os
# import re
import subprocess

# 輸入C++的編譯後程式名稱(目前失敗)
# my_cpp_code_exe = "'./"+input("C++的編譯後程式名稱：")+"'"
# print(my_cpp_code_exe)

# 判斷路徑輸入路徑是否存在，若不存在則繼續要求輸入
while True:
    try:
        # 輸入測資資料夾編號
        question_number = input("請輸入測資資料夾編號：")
        # 設置 .in 和 .out 文件夾的路徑
        input_dir = './problem_'+question_number+'_test_cases'
        output_dir = './problem_'+question_number+'_test_cases'
        # 檢查路徑是否存在
        if not os.path.exists(input_dir):
            raise FileNotFoundError
        # 如果路徑存在，就中斷迴圈
        break
    except FileNotFoundError:
        print("指定的路徑不存在，請檢查路徑是否正確")


# 獲取 .in 文件夾中的所有文件名
input_files = os.listdir(input_dir)

# 遍歷每個 .in 文件，執行 C++ 程序並將輸出保存到對應的 .out 文件中
for input_file in input_files:
    # 確定 .in 文件的完整路徑
    input_path = os.path.join(input_dir, input_file)

    # 確定 .out 文件的完整路徑
    output_file = input_file.replace('.in', '.out')
    output_path = os.path.join(output_dir, output_file)

    # 讀取 .in 文件中的輸入
    with open(input_path, 'r',encoding='utf-8') as f:
        input_data = f.read()

    # 執行 C++ 程序並獲取輸出
    result = subprocess.run(['./Q1'], input=input_data.encode(), stdout=subprocess.PIPE)
    # result = subprocess.run([my_cpp_code_exe], input=input_data.encode(), stdout=subprocess.PIPE)

    # 測試1：失敗
    # # 執行 C++ 程序並獲取輸出
    # result = subprocess.run(['./Q1'], input=input1_data.encode(), stdout=subprocess.PIPE)
    
    # # 使用正則表達式去除多於的換行符號
    # output = re.sub(r'\n+', '\n', result.stdout.decode())
    
    # # 將輸出寫入到 .out 文件中
    # with open(output_path, 'w') as f:
    #     f.write(output.rstrip())
        
    # 測試2：失敗
    # # 將輸出寫入到 .out 文件中
    # with open(output_path, 'wb') as f:
    #     f.write(result.stdout.rstrip() + b'\n')
    
    # 測試3：可以用於沒有中文的情況
    # 將輸出寫入到 .out 文件中
    if no_zh_output:
        with open(output_path, 'wb') as f:
            f.write(result.stdout)
        
    # 測試4：可以有中文輸出(會導致無中文輸出測資有換行時多換一行)
    # 將輸出寫入到 .out 文件中
    else :
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.stdout.decode('big5'))

print("完成")