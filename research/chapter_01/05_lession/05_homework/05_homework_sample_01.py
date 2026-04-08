import os
import time

# 1. Cục gạch chuyên Xóa màn hình & In tiêu đề
def in_giao_dien():
    os.system("cls" if os.name == "nt" else "clear")
    print("🚀 HE THONG PHAN CHIA NANG LUONG ORION")
    print("---------------------------------------")

# 2. Cục gạch chuyên Nhập số (Tái sử dụng được nhiều lần)
def nhap_so(prompt, kieu_du_lieu=int):
    while True:
        try:
            return kieu_du_lieu(input(prompt))
        except ValueError:
            print(f"❌ Loi: Vui long nhap {kieu_du_lieu.__name__}!")

# 3. Cục gạch Logic chính (Trái tim của App)
def xu_ly_giao_dich(total_energy):
    room = nhap_so("\n[Nhap so phong cua ban]: ", int)
    receive = nhap_so("[Nhap so nang luong ban can]: ", float)

    # Chặn lỗi logic
    if room <= 0:
        print("⚠️ Phong so 0 hoac am khong ton tai!")
        return total_energy
    
    if receive <= 0:
        print("⚠️ Gion mat? Nang luong phai lon hon 0!")
        return total_energy

    if receive > total_energy:
        print(f"❌ Khong du nang luong! (Con lai: {total_energy:.2f})")
        return total_energy

    # Giao dịch thành công
    new_total = total_energy - receive
    print(f"✅ Phong {room} da nhan {receive} units.")
    print(f"🛰️ Tram me con lai: {new_total:.2f}")
    return new_total

def main():
    nang_luong_kho_chua = 10000.0
    while True:
        try:
            in_giao_dien()
            # Goi ham xu ly va cap nhat lai nang luong
            nang_luong_kho_chua = xu_ly_giao_dich(nang_luong_kho_chua)
            
        except KeyboardInterrupt:
            print("\n🛑 NGAT KET NOI. HEN GAP LAI!")
            break
        
        time.sleep(3)

main()