import json
import os
print("Current working directory:", os.getcwd())
# x = '{ "name":"John", "age":30, "city":"New York"}'

# get = json.loads(x)
# print(get)

# data_python = {'nama': 'Ani', 'umur': 30}
# data_json = json.dumps(data_python)
# # print(data_json)
# print(json.dumps(data_python, indent=4))

with open(r'c:\laragon\www\New folder\New\data.json', 'r') as f:
    data = json.load(f)
print(data)
print(data["nama"])

# with open('data.json', 'r') as f:
#     data = json.load(f)
# print(data)

data = {'nama': 'Sari', 'umur': 27}

with open('data_output.json', 'w') as f:
    json.dump(data, f, indent=4)