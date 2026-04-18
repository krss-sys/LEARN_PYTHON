import os


def all_task():
    try:
        with open("data/06_data/06_todo_log.txt", "r", encoding="utf-8") as f:
            stt = 1
            for line in f:
                print(f"{stt}. {line.strip()}")
                stt += 1
            if stt == 1:
                print("Hien tai chua co du lieu")
    except FileNotFoundError:
        print("Hien tai chua co du lieu")

def add_task():
    new_task = input("Nhap noi dung cong viec:\n")
    with open("data/06_data/06_todo_log.txt", "a", encoding="utf-8") as f:
        f.write(new_task +"\n")
        print("Da them thanh cong")

def del_task():
    with open("data/06_data/06_todo_log.txt", "w", encoding="utf-8") as f:
        pass
    print("Da xoa toan bo danh sach")

def del_only():
    try:
        with open("data/06_data/06_todo_log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(lines)
        choice = int(input("Nhap dong can xoa: "))
        del lines[choice - 1]
        with open("data/06_data/06_todo_log.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("Da xoa")
    except ValueError:
        print("Vui long nhap so")

def read_task():
    n = int(input("Nhap so thu tu dong muon doc: "))
    with open("data/06_data/06_todo_log.txt", "r", encoding="utf-8") as f:
        stt = 1
        for line in f:
            if stt == n:
                print(f"Dong {n}: {line.strip()}")
                break
            stt += 1
        else:
            print(f"Khong co dong so {n}")

def dem_cv():
    with open("data/06_data/06_todo_log.txt", "r", encoding="utf-8") as f:
        dem = 0
        for line in f:
            if line.strip() != "":
                dem +=1
        print(f"Tong so cong viec la: {dem}")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("NOTEBOOK")
        print("================================")
        print("Phim 1. Xem tat ca cong viec")
        print("Phim 2. Them cong viec")
        print("Phim 3. Xoa toan bo danh sach")
        print("Phim 4. Xoa cong viec cu the")
        print("Phim 5. Doc 1 dong cu the")
        print("Phim 6. Dem so luong cong viec")
        print("Phim 7. Thoat")
        print('================================\n')
        choice = int(input("Hay nhap phim: "))
        if choice == 1:
            all_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            del_task()
        elif choice == 4:
            del_only()
        elif choice == 5:
            read_task()
        elif choice == 6:
            dem_cv()
        elif choice == 7:
            print("Da thoat chuong trinh")
            break
        else:
            print("Vui long chon dung phim")
        if choice != 7:
            input("Nhan enter de tiep tuc")
main()
