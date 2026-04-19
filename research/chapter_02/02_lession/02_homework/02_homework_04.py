import json

nguoi_dung = {
    "id":1,
    "name":"Bình",
    "active":True
}
with open("LEARN_PYTHON/data/chapter_02/02_data/user.json", "w", encoding="utf-8") as f:
    json.dump(nguoi_dung, f, indent=4, ensure_ascii=False)

with open("LEARN_PYTHON/data/chapter_02/02_data/user.json", "r", encoding="utf-8") as f:
    infor = json.load(f)
    print(infor)
    print(infor['name'])
    print(type(infor))
