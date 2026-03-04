import random
import time
import os

# Ham xu li nhiet do
def use_fire_extinguisher(temp):
    if temp >= 80:
        temp = 40
        print("[BINH CHUA CHAY] da giam nhiet do")
    else :
        print("[BINH CHUA CHAY] chua can dung")
    return temp
# Ham xu li chinh
def run_bot():
    temp = 50
    bot_active = True
    while bot_active:
        os.system("cls" if os.name== "nt" else "clear" )
        temp += random.randint(3,5)
        print(f"nhiet do hien tai:{temp} °C")
        temp = use_fire_extinguisher(temp)
        time.sleep(1)
        if temp > 100:
            print("MAY PHAT NO")
            bot_active = False
run_bot()
