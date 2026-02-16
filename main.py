import os
import time
import psutil
try:
    while True:
        os.system('cls')
        print("-----Tình trạng RAM-----")
        #Lấy thông tin RAM
        mem=psutil.virtual_memory()
        #Quy ước biến
        total=mem.total/(1024**3)
        available=mem.available/(1024**3)
        percent=mem.percent
        used=mem.used/(1024**3)
        #Thông báo
        print(f"|Tổng RAM|:{total:.2f}GB,\n|Đã dùng|:{used:.2f}GB,\n|Còn trống|:{available:.2f}GB,\n|Phần trăm sử dụng|:{percent}%")
        #Thời gian nghỉ
        time.sleep(2)
except KeyboardInterrupt:
    print("\n -----Kết thúc tiến trình-----")
