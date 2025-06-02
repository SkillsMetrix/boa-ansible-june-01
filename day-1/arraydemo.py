
userNames=['admin','Manager','QA']

for uname in userNames:
    print(uname)

# print data with index position

for index, uname in enumerate(userNames):
    print(f" Index: {index}, -> {uname.upper()} ")
