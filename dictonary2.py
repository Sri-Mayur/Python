d={"Name":"Mayur", "Age":18, "Location": "Zila Ghaziabad"}

d.pop("Location")
print(d)
d["Phone Number"]=8757685
print(d)

d.setdefault("Marks")
print(d)

print(d.popitem())
print(d)

d1=d.copy()
print(d1)