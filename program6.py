employees = ['sabiha','joshna','jeevana']
defaults = {"designstion": 'Developer',"salary":80000}

data = dict.fromkeys(employees,defaults)
print(data)

print(data["sabiha"])
