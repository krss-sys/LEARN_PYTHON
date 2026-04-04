import time
while True:
    try: 
        with open("file/nhat_ky.txt", "a", encoding = "utf-8") as f:
            noi_dung_moi = input("Hom nay ban da lam gi: \n")
            f.write(noi_dung_moi +"\n")
        with open("file/nhat_ky.txt", "r", encoding="utf-8") as f:
            noi_dung = f.read()
            print(f"{noi_dung}")
    except KeyboardInterrupt:
        print("Cuong che thoat chuong trinh")
        break
    time.sleep(2)    
