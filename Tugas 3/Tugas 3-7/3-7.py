name=['chloe grace moretz','kyrie irving','eiza gonzales']
a=('i would like to invite')
b=('to dinner')
print(a,name[0],b)
print(a,name[1],b)
print(a,name[2],b)

print('eiza cannot come')
name[2]='taylor swift'
print(a,name[0],b)
print(a,name[1],b)
print(a,name[2],b)
print("there will be another guests")
name.insert(0,"roy")
name.insert(3,"mill")
name.insert(5,"rory")

print(a,name[0],b)
print(a,name[3],b)
print(a,name[5],b)
print(a,name[4],b)
print(a,name[1],b)
print(a,name[2],b)
print("there's been a change")
name.pop()
name.pop()
name.pop()
name.pop()
print(name)
print("only",name[0],"and",name[1],"will be coming")
print("im sorry kyrie, eiza, rory, mill because you are no longer invited")
del name[0]
del name[0]
