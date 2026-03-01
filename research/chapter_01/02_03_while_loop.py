"""
import time

# Vòng lặp vô hạn
while True:
    print("Aoi đang chạy ngầm...")
    time.sleep(2) # Dừng 2 giây để đỡ tốn CPU
"""

import time
import random

# Gia lap phan cung
cpu_temp = 50
bot_active = True # Bien dieu kien

# Vong lap dung bien dieu kien
while bot_active:
    print(f"Bot đang kiểm tra nhiệt độ:{cpu_temp}°C")

    # Gia lap nhiet do thay doi
    cpu_temp += random.randint(-2,6)

    # Dung if/else
    if cpu_temp > 60:
        print("Nhiệt độ quá cao! Bot đang tự ngắt...")
        bot_active = False # Điều kiện sai
    # thoi gian nghi
    time.sleep(1)
    print("Bot đã dừng hoàn toàn")
