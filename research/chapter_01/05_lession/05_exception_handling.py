"""
import time

def monitor_system():
    print("--- TRẠM KIỂM SÁT ĐANG KHỞI ĐỘNG ---")
    
    while True:
        try:
            # Giả lập nhập chỉ số từ cảm biến (user nhập)
            temp = input("\nNhập nhiệt độ lõi (hoặc gõ 'exit' để dừng): ")
            
            if temp.lower() == 'exit':
                break
                
            temp = float(temp) # Dòng này dễ gây lỗi ValueError nếu nhập chữ
            
            if temp > 100:
                print("⚠️ CẢNH BÁO: Nhiệt độ quá cao!")
            else:
                print(f"✅ Nhiệt độ ổn định: {temp}°C")
                
        except ValueError:
            print("❌ LỖI CẢM BIẾN: Dữ liệu nhiệt độ không hợp lệ. Vui lòng nhập số!")
            
        except KeyboardInterrupt:
            # Bắt lỗi khi mày nhấn Ctrl + C để dừng chương trình
            print("\n🛑 Ngắt kết nối khẩn cấp từ người dùng!")
            break
            
        finally:
            print("--- System check completed ---")
            time.sleep(1)

monitor_system()
"""

import time
import os

def so_tuoi_nguoi_yeu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            print("---APP TINH TUOI NGUOI YEU CUA BAN---")
            tuoi = input("\nSo tuoi cua nguoi yeu ban la: ")
            tuoi = int(tuoi)
            print(f"The thi nguoi yeu ban dang {tuoi} tuoi")
            break
        except ValueError:
            print("DM T BAO LA NHAP SO TUOI KO PHAI CHU")
        except KeyboardInterrupt:
            print("APP DA DUNG HOAT DONG")
            break
        finally:
            print("by KRSS")
            time.sleep(2)
so_tuoi_nguoi_yeu()