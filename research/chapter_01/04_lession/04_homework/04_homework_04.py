import os
import time
import random

def check_security(code):
    if code == "hacker_vip":
        return True
    else:
        return False

def start_countdown():
    try:
        for i in range(5,0,-1):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"He thong se mo sau {i}...")
            time.sleep(1)
        return True
    except KeyboardInterrupt:
        print("Cuong che thoat chuong trinh")
        return False

def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("BATTLESHIP ACCESS")
            print("\n============================")
            print("|Phim 1: Nhap ma truy cap  |")
            print("----------------------------")
            print("|Phim 2: Thoat chuong trinh|")
            print("============================\n")
            choice = input("Hay chon chuong trinh: ")
            if choice == "1":
                password = input("\nHay nhap mat khau: ")
                if check_security(password):
                    ket_qua = start_countdown()
                    if ket_qua:
                        print("Da dang nhap thanh cong")
                        break
                else:
                    print("Sai mat khau. Vui long thu lai")
            elif choice == "2":
                print("Tam biet")
                break
            elif choice == "":
                print("Khong duoc de trong")
            else:
                print("Chi chon 1 hoac 2")
        finally:
            print("---Ket thuc phien lam viec---")
        time.sleep(2)
main()
