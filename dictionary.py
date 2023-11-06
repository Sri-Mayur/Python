d={"Name":"Virat Kohli","Score":101, "Name":"Dhruv Kumar"}
d2={"Player":"Macbook", "Type":"Viper"}
d3={"Player3":"Present Sir", "Type": "Audacity"}

d.update(d2)
d.update(d3)
d.pop("Player")
d.clear()

print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.items())

#Key is immutable however Value can be changed

