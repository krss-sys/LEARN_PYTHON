import random
import os
import time

# 1. Quy trinh hoat dong
def mine_resources(energy,minerals):
    energy -= 10
    minerals += random.randint(5,10)
    return energy,minerals

# 2. quy trinh sua chua
def repair_robot(energy,health):
    if health <= 50 and energy >= 30:
        health += 25
        energy -= 20
        print("Dang sua chua")
    return health,energy
# 3. Kiem tra he thong
def check_status(energy, health, minerals):
    # 1. Kiểm tra từng lý do thất bại riêng biệt
    if energy <= 0:
        print("STOP: Robot het nang luong!")
        return False # Cút luôn, đéo check mấy cái dưới nữa
        
    if health <= 0:
        print("EXPLODE: Robot bi hu hong nang!")
        return False # Cút luôn
        
    # 2. Kiểm tra điều kiện thắng
    if minerals >= 50:
        print("HOAN TAT QUA TRINH KHAI THAC")
        return False
        
    # 3. Nếu đéo dính cái nào ở trên -> Robot vẫn ổn
    print("Robot dang lam viec...")
    return True

# 4. MAIN
def run_bot():
    energy = 100
    minerals = 0
    health = 100
    bot_active = True

    while bot_active:
        # Dao khoang
        os.system("cls" if os.name == "nt" else "clear")
        energy, minerals = mine_resources(energy,minerals)

        # Kiem tra tinh trang
        health -= random.randint(1,5)
        health, energy = repair_robot(energy, health)

        # In thong so
        print("-"*20)
        print(f"Tinh trang tau hien tai: {health} %")
        print(f"Nang luong cua tau hien tai: {energy} %")
        print(f"So khoang san dao duoc: {minerals} vien")
        print("-"*20)

        # Check xem bot chay dc ko
        bot_active = check_status(energy,health,minerals)

        time.sleep(2)
run_bot()
        