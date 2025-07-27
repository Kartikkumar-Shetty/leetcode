f = open("file.txt")
data = f.read()
d1 = data.split("\n")

print(f"{d1[0]} is his fn and {d1[1]} is his ln and lives at {d1[2]}")
print(d1[0],"is his fn and", d1[1],"is his ln and lives at", d1[2])