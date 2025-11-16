
sport = ["football", "basketbal", "tb-tennis", "golf"]

print(sport[0])
print(len(sport))

list1 = [1 ,3 , 5, 7, 9,]
list2 = [True, False, True]

print(type(list))
print(type(list2[2]))

tl = list(("ap", "bnn", "cr"))
print(tl)

print(sport[-1])

f = ["ap", "bnn", "cr", "or", "kw", "mg"]
print(f[2:5])

print(f[:4])

print(f[2:])

if "ap" in f:
    print("have apple")


f[1] = "ccn"

print(f)

f.append("g")
print(f)

f.insert(1, "wtml")
print(f)

f2 = ["wtml", "grape", "ccn"]
f.extend(f2)
print(f)

f.remove("or")
print(f)

f.pop(1)
print(f)

f.pop()
print(f)