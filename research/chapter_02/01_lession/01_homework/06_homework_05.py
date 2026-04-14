import json
import os

def load():
    try:
        with open("file/06_07_lession/exam.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except:
        return {"money" : 0}
def save(data):
    with open("file/06_07_lession/exam.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Da luu du lieu")

def calculation(so_tien):
    du_lieu = load()
    phep_tinh = input("Ban muon tru tien hay cong tien.\nNeu cong dung phim 1.\nNeu tru dung phim 2\n")
    if phep_tinh == "1":
        du_lieu['money'] += so_tien
        save(du_lieu)
    elif phep_tinh == "2":
        if so_tien > du_lieu['money']:
            print("Ko du tien")
        else:
            du_lieu['money'] -= so_tien
        save(du_lieu)
    else:
        print("loi du lieu")

def write_log(noi_dung):
    with open("file/06_07_lession/xamlon.txt", "a", encoding="utf-8") as f:
        f.write(noi_dung + "\n") # Thêm \n để mỗi lần ghi là một dòng mới

def read_log():
    with open("file/06_07_lession/xamlon.txt", "r", encoding="utf-8") as f:
        noidung = f.read()
        print(noidung)

def main():

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("He thong xam lon")
        print("===============================")
        print("Phim 1. Cong tru tien")
        print("Phim 2. Xem du lieu")
        print("Phim 3. Tao nhat ki")
        print("Phim 4. Check nhat ki")
        print("Phim 5. Thoat")
        print("===============================\n")
        choice = input("Hay nhap phim tat: ")
        if choice == "1":
            so_tien = int(input("Hay nhap so tien: "))
            calculation(so_tien)
            ket_qua = load()
            print(ket_qua)
        elif choice == "2":
            ket_qua = load()
            print(ket_qua)
        elif choice == "3":
            noi_dung = input("Nhat ki: ")
            ket_qua = write_log(noi_dung)
        elif choice == "4":
            read_log()
        elif choice ==  "5":
            print("Thoat")
            break
        else:
            print("Vui long nhap dung phim tat")
        if choice != "5":
            input("Nhan enter de tiep tuc...")
main()


