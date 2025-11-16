name = "HelloEDco"

# 1. หาความยาวรวม: ใช้ len()
length = len(name)
print(f"total lenght = {length} letter")

print("-" * 25)
for i, char in enumerate(name):
    print(f"'{char}'")