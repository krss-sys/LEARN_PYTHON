import os
import random
import time

def main():
    total_energy = 10000
    while True:
        try:
           os.system("cls" if os.name == "nt" else "clear")
           print("HE THONG PHAN CHIA NANG LUONG")
           print("-----------------------------------")
           room = input("\n[nhap so phong cua ban]: ")
           room = int(room)
           receive_energy = input("[nhap so nang luong ban can]: ")
           receive_energy = float(receive_energy)
           if receive_energy >= total_energy:
               print("KO DU NANG LUONG CUNG CAP")
           if room == 0:
               print("co phong 0 a ?")
           elif receive_energy <= 0:
               print("gion mat?")         
           else:
               total_energy = total_energy - receive_energy
               print(f"---cam on phong so {room} da su phong dich vu cung cap nang luong---")
               print(f"---nang luong con lai cua tram khong gian la:{total_energy:.2f}---")
        except ValueError:
            print("\nso phong: xin hay nhap so nguyen")
            print("so nang luong: xin hay nhap so thuc")
        except ZeroDivisionError:
            print("vui long ko nhap so 0")
        except KeyboardInterrupt:
            print("CAM ON DA SU DUNG DICH VU")
            break
        except Exception as e:
            print(f"loi:{e}")
        time.sleep(5)
main()


