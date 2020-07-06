#Same like List

tup=("1","2","3","4","5")

print(tup)

for t in tup:
    print(t)

print("--------------")
print(max(tup))
print("--------------")
print(min(tup))
print("--------------")

to=0
for t in tup:
    to=to+int(t);

print("total",to)

print("--------------")

print("Average",to/len(tup))
