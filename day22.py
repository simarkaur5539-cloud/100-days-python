lst1=[1,2,3]
lst2=["red",'blue','green']
print(lst1+lst2)
dict={"name":"simar","age":20}
print(dict)
print(lst1[0])
print(lst2[-1])
col=['bee','hell','fun']
if 'bee'in col:
    print("yes")
else:
    print("no")
print(col[0:2])
names=["milo","simar","kaur","detent"]
names_3=[item for item in names if(len(item)>3)]
print(names_3)