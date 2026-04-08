import random
import time
import os

def doc_nhiet_do():
    while True:
        try:
            nhiet_do = input("\nNhap nhiet do hien tai cua Tram: ")
            return float(nhiet_do)
        except ValueError:
            print("Hay nhap kieu du nhieu so")

def chia_nang_luong():
    try:
        so_khoang = int(input("Hay nhap so luong khoan can chia nang luong: "))
        tong_e = float(input("Nhap so nang luong can: "))
        ket_qua = tong_e/ so_khoang
        return ket_qua,tong_e
    except ZeroDivisionError:
        print("so khoan phai khac 0")
        return 0,0
    except ValueError:
        print("Phai nhap so")
        return 0,0

def gui_tin_hieu():
    try:
        noi_dung = input("Nhap tin nhan: ")
        if noi_dung == "":
            raise Exception("Tin nhan rong")
        print(f"Dang gui:{noi_dung}")
        time.sleep(1)
        print("---Da gui thanh cong---")
    except Exception as e:
        print(f"Loi lien lac: {e}")
    finally:
        print("Da ngat ket noi voi trai dat")

def tu_huy():
    try:
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        print("Tu huy hoan tat")
        return "thoat"
    except KeyboardInterrupt:
        print("Dung tu huy")
        return None

def main():
    tong_elec = 1000000
    while True:
        try:
            print("\nMENU HE THONG")
            print("========================")
            print("1. He thong nhiet do")
            print("2. He thong nang luong")
            print("3. He thong lien lac")
            print("4. He thong tu huy")
            print("0. Thoat chuong trinh")
            print("========================")
            choice = int(input("Moi ban chon he thong su dung: "))
            if choice == 1:
                nhiet_do_tram = doc_nhiet_do()
                print(f"nhiet do la : {nhiet_do_tram}")
            elif choice == 2:
                nang_luong_da_dung, nang_luong_tieu_thu = chia_nang_luong()
                if nang_luong_tieu_thu > tong_elec:
                    print("Ko du nang luong")
                elif nang_luong_tieu_thu <=0:
                    print("Giao dich ko thanh cong")
                else:
                    print(f"Da chia nang luong, Moi khoan co {nang_luong_da_dung:.2f}")
                    tong_elec = tong_elec - nang_luong_tieu_thu
                    print(f"So nang luong con lai: {tong_elec}")
            elif choice == 3:
                gui_tin_hieu()
            elif choice == 4:
                ket_qua = tu_huy()
                if ket_qua == "thoat":
                    break
            elif choice == 0:
                print("Dang thoat...")
                time.sleep(2)
                print("----Da thoat----")
                break
            else:
                print("Dm nhap tu 0 den 4 thoi")
        except ValueError:
            print("Xin hay nhap so")    
        except KeyboardInterrupt:
            print("Cuong che thoat chuong trinh")
            break
        except Exception as e:
            print(f"Loi: {e}")
        time.sleep(1)
main()



