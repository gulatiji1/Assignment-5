orignal_list=[]
for i in range(1,11):
    orignal_list.append(i)

print(f"Orignal_list={orignal_list}")
Extracted=orignal_list[0:5:1]
print(f"Extracted list-{Extracted}")
Reversed=[]
for i in range(len(Extracted)-1,-1,-1,):
    Reversed.append(Extracted[i])

print(f"Revered-{Reversed}")
