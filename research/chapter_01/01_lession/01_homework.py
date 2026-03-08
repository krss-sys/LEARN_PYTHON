raw_data = "26"
raw_salary = 1250.75
exchange_rate = "25450"
is_manager = True

# Tính số tuổi 5 năm sau
print(f"Số tuổi của Krss 5 năm sau:{int(raw_data)+5}")

# Tính lương VND
print(f"Số lương quy đổi sang VND:{int(exchange_rate)*raw_salary} (VND)")

# Làm tròn lương
luong_le = int(exchange_rate)*raw_salary
print(f"Lương làm tròn là:{int(luong_le)}(VND)")

# Xuất dữ liệu
ten_nhan_vien = "krss"
print(f"Nhân viên:{ten_nhan_vien} | Quản lí:{bool(is_manager)} | Tuổi 5 năm tới:{int(raw_data)+5} | Lương:{int(luong_le)} VND")

