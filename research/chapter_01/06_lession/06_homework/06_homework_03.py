import time
import os
import random
import json

def add_member(name,money):
    new_id = random.randint(100000,999999)
    money = int(money)
    if money >= 2000000:
        rank = "Gold"
    elif money >= 1000000:
        rank = "Silver"
    elif money >= 500000:
        rank = "Bronze"
    else:
        rank = "Unrank"
    new_member = {
        "ID"        : new_id,
        "Name"      : name,
        "Balance"   : money,
        "Rank"      : rank
    }
    print("\nDu lieu cua ban da duoc tao")
    print(f"ID tai khoan: {new_id} | * chu y nho id de tra cuu tai khoan")
    print(f"Ten chu tai khoan: {name}")
    print(f"So tien da nap: {money} VND")
    print(f"Muc ranh hien tai: {rank}")
    return new_member

def save_data(all_member):
    with open("file/06_lession/members.json", "w", encoding="utf-8") as f:
        json.dump(all_member, f, indent=4, ensure_ascii= False)

def load_data():
    try:
        with open("file/06_lession/members.json", "r", encoding="utf-8") as f:
            return json.load(f) # Bốc toàn bộ dữ liệu từ file ra
    except:
        return {} # Nếu file chưa có hoặc bị lỗi, trả về cái Dict rỗng để app không sập

def nap_tien(data, id, money):
    id = str(id)
    if id in data:
        old_balance = data[id]["Balance"]
        new_balance = old_balance + money
        data[id]["Balance"] = new_balance
        if new_balance >= 2000000:
            data[id]["Rank"] ="Gold"
        elif new_balance >= 1000000:
            data[id]["Rank"] = "Silver"
        elif new_balance >= 500000:
            data[id]["Rank"] = "Bronze"
        else:
            data[id]["Rank"] = "Unrank"
        print(f"Nap thanh cong. So du moi cua {data[id]['Name']} la: {new_balance}\nRank hien tai: {data[id]['Rank']}")
        return data
    else:
        print("Khong tim thay id nguoi dung")
        return data

def truy(data,id):
    id = str(id)
    if id in data:
        print(f"Ten thanh vien: {data[id]['Name']}")
        print(f"So tien hien con: {data[id]['Balance']} VND")
        print(f"Muc rank hien tai: {data[id]['Rank']}")
        return data
    else:
        print("Khong co id trung khop")
        return data

def xoa_tk(id, data):
    id = str(id)
    if id in data:
        ten_bi_xoa = data[id]["Name"]
        print(f"{ten_bi_xoa} co muon xoa tai khoan khong? Nhan Y de xoa, nhan N de thoat")
        lenh = input()
        if lenh == "y" or lenh == "Y":
            data.pop(id)
            print("Tai khoan da bi xoa")
        elif lenh == "n" or lenh == "N":
            print("Tai khoan van chua bi xoa")
        else:
            print("Vui long nhap dung ki tu")
        return data
    else:
        print("id khong hop le")
        return data
def main():
    all_members = load_data()
    while True:
        os.system("cls" if os.name =="nt" else "clear")
        print("GAMING CENTER")
        print("-----------------------------")
        print("Phim 1. Dang ki thanh vien")
        print("Phim 2. Tra cuu tai khoan")
        print("Phim 3. Nap tien")
        print("Phim 4. Xoa tai khoan")
        print("Phim 5. Thoat")
        print("-----------------------------\n")
        choice = input("Hay nhap lua chon: ")
        if choice == "1":
            ten = input("Hay nhap ten: ")
            so_tien = int(input("Hay nhap so tien de duy tri tai khoan: "))
            new_mem = add_member(ten, so_tien)
            all_members[str(new_mem["ID"])] = new_mem
            save_data(all_members)
        elif choice == "2":
            id_tim = input("Nhap id: ")
            truy(all_members, id_tim)
        elif choice == "3":
            id_nap = input("Nhap id tai khoan can nap: ")
            tien = int(input("So tien can nap: "))
            nap_tien(all_members, id_nap, tien)
            save_data(all_members)
        elif choice == "4":
            id_xoa = input("Nhap id tai khoan can xoa: ")
            xoa_tk(id_xoa, all_members)
            save_data(all_members)
        elif choice == "5":
            print("Da thoat chuong trinh")
            break
        else:
            print("Vui long nhap dung phim tat")
        if choice !="5":
            input("Nhan Enter de tiep tuc")
    time.sleep(1)
main()    


