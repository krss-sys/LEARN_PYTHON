# --- BƯỚC 1: GHI ĐÈ (WRITE) ---
with open("file/data_krss.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1: Đây là nội dung cũ.\n")

# --- BƯỚC 2: GHI THÊM (APPEND) ---
with open("file/data_krss.txt", "a", encoding="utf-8") as f:
    f.write("Dòng 2: Đây là nội dung mới được thêm vào!\n")

# --- BƯỚC 3: ĐỌC FILE (READ) ---
with open("file/data_krss.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read() # Đọc hết cả file
    print("Nội dung file hiện tại là:")
    print(noi_dung)