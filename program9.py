sample_dict = {
    "name": "kelly",
    "age":25,
    "salary":8000,
    "city": "New york"}
keys=["name","salary"]


for k in keys:
    sample_dict.pop(k)
print(sample_dict)
