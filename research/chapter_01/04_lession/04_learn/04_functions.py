import time
import os
import random

# 1.Ham cap nhat tham so
def update_stars(energy, temp):
    energy -= random.randint(1,5)
    temp += random.randint(-2,7)
    return energy,temp

# 2.Ham kiem tra va in trang thai
def check_status(energy, temp):
    if energy <= 0 or temp >= 90:
        if energy <= 0:
            print("Status: Het pin, sap nguon")
        else:
            print("Satus: Chay may, sap nguon")
        return False
    
    if energy <= 20:
        print("Pin yeu, tim nguon sac")
    if temp >=70:
        print("Qua nong, bat tan nhiet")
    return True

# 3.Ham chinh dieu khien
def run_bot():
    energy = 100
    temp = 40
    bot_active = True

    while bot_active:
        os.system("cls" if os.name=="nt" else "clear")
        energy, temp = update_stars(energy, temp)
        print("-----Bot dang tuan tra-----")
        print("[Pin: {}% | nhiet: {}°C]".format(energy, temp))
        bot_active = check_status(energy, temp)
        time.sleep(0.5)
run_bot()
