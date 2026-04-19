import json

mon_hoc = {
    "ten":"python",
    "so_tin":3,
    "online":True,
    "ten_hv":"Huỳnh Tuấn Kiệt"
}

infor = json.dumps(mon_hoc, indent = 4, ensure_ascii=False)
print(infor)
print("----------------")
print(json.dumps(mon_hoc))
print("----------------")
print(json.dumps(mon_hoc, indent=4, ensure_ascii=False))
print("--------------------------")
print(type(infor))