import time
import os
import random
import json
list = {}

def input_product(name, id, so_luong, gia):
    global list
    if id in list:
        print(f"Cap nhat them san pham: {name}")
        print(f"Code: {id}")
        print(f"So luong cong them: {so_luong}.")
        list[id]["Luong_hang"] += so_luong
        print(f"Tong so luong hien co: {list[id]['Luong_hang']}")
        return list
    else:
        list[id] = {
            "Name"          :   name,
            "Code"          :   id,
            "Luong_hang"    :   so_luong,
            "Gia"           :   gia
        }
        print("\nDa nhap danh sach hang hoa")
        print(f"Ten hang hoa: {list[id]['Name']}")
        print(f"Ma code: {list[id]['Code']}| Luu y ghi nho ma code de tra cuu")
        print(f"So luong hang: {list[id]['Luong_hang']}")
        print(f"Gia hang hoa: {list[id]['Gia']}")
        return list

def output_product(id,so_luong):
    if id in list:
        if so_luong <= list[id]["Luong_hang"]:
            print(f"Da cap nhat tinh trang san pham: {list[id]['Name']}")
            print(f"CODE: {list[id]['Code']}")
            print(f"SO luong hang da duoc mua: {so_luong}")
            list[id]["Luong_hang"] -= so_luong
            print(f"So luong hang con lai: {list[id]['Luong_hang']}")
            return list
        else:
            print("Hien tai kho khong du hang")
            return list
    else:
        print("code sai")
        return list
    
def truy(id):
    if id in list:
        print(f"Thong tin san pham: {list[id]['Name']}")
        print(f"CODE: {list[id]['Code']}")
        print(f"So luong hien co: {list[id]['Luong_hang']}| Gia tri moi san pham: {list[id]['Gia']}")
        tong_tien = list[id]['Luong_hang'] * list[id]['Gia']
        print(f"Tong gia tri ton kho: {tong_tien:.2f} VND")
        return list
    
def load():
    try:
        with open("file/06_lession/data.json", "r", encoding="utf-8") as f:
            list = json.load(f)
            return list
    except:
        list = {}
        return list

def save(list):
    with open("file/06_lession/data.json", "w", encoding="utf-8") as f:
        json.dump(list, f, indent=4)

def main():
    global list
    list = load()
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("HE THONG QUAN LI KHO HANG")
            print("=================================")
            print("Phim 1. Nhap moi don hang & them hang vao kho")
            print("Phim 2. Ban hang")
            print("Phim 3. Truy xuat thong tin don hang")
            print("Phim 4. Luu du lieu")
            print("Phim 5. Thoat")
            print("=================================\n")
            choice = input("Hay nhap phim dich vu: ")
            if choice == "1":
                name = input("Nhap ten san pham: ")
                code = str(input("Tu tao code co 6 chu so cho sp moi: "))
                print(f"Code cua san pham la: {code}| Luu y ghi nho id nay")
                so_luong = int(input("Nhap so luong hang: "))
                gia = float(input("Nhap gia tren moi san pham: "))
                thong_tin = input_product(name, code, so_luong, gia)
            elif choice == "2":
                id = input("Nhap code san pham: ")
                so_sp = int(input("Nhap so luong can ban: "))
                ket_qua = output_product(id, so_sp)
            elif choice == "3":
                code = input("Hay nhap id san pham de truy xuat: ")
                ket_qua = truy(code)
            elif choice == "4":
                save(list)
            elif choice == "5":
                print("Thoat chuong trinh")
                break
            else:
                print("Phim tat ko hop le")
            if choice != "5":
                input("Nhan enter de tiep tuc: ")
        except KeyboardInterrupt:
            print("Da thoat chuong trinh")
    time.sleep(1)        
main()


