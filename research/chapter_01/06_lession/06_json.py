import json

data = {
    "ten": "Krss",
    "level": 6,
    "is_hacker": True,
    "skills": ["Python", "Logic", "File Handling"]
}

with open("file/user_profile.json", "w", encoding="utf-8") as f:
    # dump(biến_dữ_liệu, file_f, indent=4)
    json.dump(data, f, indent=4, ensure_ascii=False)

with open("file/user_profile.json", "r", encoding="utf-8") as f:
    # load(file_f) -> trả về đúng kiểu dữ liệu ban đầu
    du_lieu_moi = json.load(f)

print(du_lieu_moi["ten"]) # Kết quả: Krss
print(du_lieu_moi["skills"][0]) # Kết quả: Python