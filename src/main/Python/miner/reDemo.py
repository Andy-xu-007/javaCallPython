import re

s = r'^\d{3}\-\d{3,8}$'
t = re.match(s, "101-235684")
print(t)

if t:
    print("OK")
else:
    print("error")
