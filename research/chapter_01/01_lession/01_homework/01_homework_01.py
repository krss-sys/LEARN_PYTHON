import os

def main():
    ho_ten = input("Nhap ho va ten: ")
    nam_sinh = int(input("Nhap nam sinh: "))
    chieu_cao = float(input("nhap chieu cao: "))
    nhap = input("Co phai la sinh vien khong? (true or false): ")
    
    print(f"Ho Ten: {ho_ten.strip().title()}")
    print(f"So tuoi: {2026-nam_sinh}")
    print(f"Chieu cao: {chieu_cao:.2f}")
    if nhap.lower() == "true":
        print("May la sinh vien")
    else:
        print("May deo phai sinh vien")
main()
    