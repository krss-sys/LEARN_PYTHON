ds = ["A", "B", "C"]
so = int(input("Hay nhap so dong: "))
stt = 1
for ten in ds:
    if so == stt:
        print(f"{stt}. {ten.strip()}")
        break
    stt +=1