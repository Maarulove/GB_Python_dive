pi = 3.1432323312123

print(f"{pi:.3f}")
print(f"{pi = :_}")

data = [2312, 12312, 14212, 54534]
for i in data:
    print(f"{i: >10}")
    print(f"{i =:>10}")
################################################
a, b, *_ = input("type smth").split()
print(a, b, _)
################################################
abc = ";".join(data)
print(abc)

