# import time
# import random

# energy = 100
# temp = 40
# bot_active = True

# while bot_active:
#     energy -= random.randint(1, 5)
#     temp += random.randint(-2, 8)
    
#     print("-" * 30)
#     print(f"📊 [Pin: {energy}% | Nhiệt: {temp}°C]")

#     # 🔥 LOGIC SẠCH SẼ: Ưu tiên cái chết chóc nhất lên đầu
#     if energy <= 0:
#         print("💀 STATUS: BOT SẬP NGUỒN!")
#         bot_active = False
#     elif temp > 90:
#         print("🔥 STATUS: CHÁY MÁY! TỰ TẮT KHẨN CẤP!")
#         bot_active = False
#     elif energy < 20:
#         print("🪫 WARNING: Pin yếu! Đang tìm trạm sạc...")
#     elif temp > 70:
#         print("⚠️ WARNING: Quá nóng! Đang bật tản nhiệt nước...")
#     else:
#         print("🤖 STATUS: Bot đang tuần tra...")

#     time.sleep(1)

import time
import random
import os

energy = 100
temp = 40
bot_active = True

# Vong lap pro
while bot_active:
    os.system("cls"if os.name =="nt" else "clear")
    temp += random.randint(-2,5)
    energy -= random.randint(1,5)
    print("-----Bot dang tuan tra-----")
    print(f"[Pin: {energy} % | Nhiet do: {temp} °C]")
    # Vong lap quan trong
    if energy <= 0 or temp > 90:
        if energy <= 0:
            print("Bot sap nguon")
            bot_active = False
        elif temp > 90:
            print("Qua nong tat nguon")
            bot_active = False
    # Vong lap check
    if energy <=20:
        print("Pin yeu, dang tim nguon sac")
    if temp > 70:
        print("May nong, bat tan nuoc")
    # Kiem tra
    if energy >20 and temp <= 70:
        print("-----Tinh trang on-----")
    time.sleep(2)


