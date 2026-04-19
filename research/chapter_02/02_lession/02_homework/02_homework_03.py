import json

json_str = '{"ten":"AN", "diem":9.5, "hoc_bong":false}'
data = json.loads(json_str)
print(data['diem'])

print(json.loads(json_str))
print(type(json.loads(json_str)))
