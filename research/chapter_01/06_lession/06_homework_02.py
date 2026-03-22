import os
import json

data = {
    "Name" : "Krss",
    "Code" : "007",
    "Skill" : ["Python", "Infiltration"]
}

def save_agent(data):
    with open("file/06_lession/agent_profile.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("da luu thong tin dac vu")

def load_agent():
    with open("file/06_lession/agent_profile.json", "r", encoding="utf-8") as f:
        dac_vu = json.load(f)
        print(f"Dac vu {dac_vu} da san sang!")

def write_log(action):
    with open("file/06_lession/log.txt", "a", encoding="utf-8") as h:
        h.write(action +"\n")

def read_log():
    with open("file/06_lession/log.txt", "r", encoding="utf-8") as h:
        nhat_ki_hoat_dong = h.read()
        print(nhat_ki_hoat_dong)

def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("CHUONG TRINH DAC VU")
            print("-------------------------------")
            print("Phim 1. Nhap thong tin dac vu")
            print("Phim 2. Xem thong tin dac vu hien tai")
            print("Phim 3. Nhat ki nhiem vu")
            print("Phim 4. Xem nhat ki")
            print("Phim 5. Thoat")
            print("-------------------------------\n")
            choice = int(input("Vui long nhap phim tat: "))
            if choice == 1:
                Ten_dac_vu = input("Nhap ten dac vu: ")
                new_code = input("Nhap code moi: ")
                ki_nang = input("Nhap ki nang: ")
                new_dict = {
                    "Name" : Ten_dac_vu,
                    "Code" : new_code,
                    "Skill": ki_nang
                }
                save_agent(new_dict)
            elif choice == 2:
                load_agent()
            elif choice == 3:
                ghi_nhat_ki = (input("Nhat ki hoat dong: \n"))
                write_log(ghi_nhat_ki)
            elif choice == 4:
                read_log()
            elif choice == 5:
                print("Da thoat chuong trinh")
                break
            else:
                print("Vui long nhap dung phim tat")
            if choice !=5:
                input("\n[Nhan Enter de tiep tuc...]")
        except ValueError:
            print("Vui long nhap so")
        except KeyboardInterrupt:
            print("Cuong che thoat chuong trinh")
main()

