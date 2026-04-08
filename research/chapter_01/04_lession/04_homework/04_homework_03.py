import random
import os
import time

def tieu_hao_hang_ngay(oxy, nang_luong, thuc_an):
    oxy -= 10
    nang_luong -= 5
    thuc_an -= 2
    return oxy, nang_luong, thuc_an

def he_thong_tu_dong(oxy, nang_luong, vo_tau):
    if oxy < 30:
        nang_luong -= 15
        oxy += 40
        print("Dang tao oxy")
    if vo_tau < 50:
        nang_luong -= 20
        vo_tau += 30
        print("Dang va vo tau")
    return oxy, nang_luong, vo_tau

def su_kien_ngau_nhien(oxy, nang_luong, vo_tau):
    su_co = random.randint(1,10)
    if su_co == 1:
        vo_tau -= 40
    elif su_co == 2:
        nang_luong -= 30
    return oxy, nang_luong, vo_tau

def kiem_tra_sinh_ton(oxy, nang_luong, thuc_an, vo_tau):
    if oxy <= 0:
        return False
    if nang_luong <= 0:
        return False
    if thuc_an <= 0:
        return False
    if vo_tau <= 0:
        return False
    print("Moi thu van on")
    return True

def run_station():
    oxy = 100
    nang_luong = 100
    thuc_an = 50
    vo_tau = 100
    bot_active = True
    day = 0
    while bot_active:
        os.system("cls" if os.name == "nt" else "clear")
        day += 1
        if day == 11:
            print("Ket thuc dieu tra")
            bot_active = False
        else:
            print(f"Ngay thu {day} o ngoai khong gian")
            oxy, nang_luong, thuc_an = tieu_hao_hang_ngay(oxy, nang_luong, thuc_an)
            oxy, nang_luong, vo_tau = su_kien_ngau_nhien(oxy, nang_luong, vo_tau)
            oxy, nang_luong, vo_tau = he_thong_tu_dong(oxy, nang_luong, vo_tau)
            bot_active = kiem_tra_sinh_ton(oxy, nang_luong, thuc_an, vo_tau)
            print(f"[oxy con lai: {oxy} %]")
            print(f"[Nang luong con lai: {nang_luong} %]")
            print(f"[Thuc an con lai: {thuc_an}]")
            print(f"[Tinh trang vo tau: {vo_tau} %]")
            time.sleep(1)
run_station()    
