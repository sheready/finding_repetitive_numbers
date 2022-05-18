l=[20,30,60,40,91,56,30,20,45]
l1=[]
for i in l:
  if i not in l1:
    l1.append(i)
  else:
    print(i,end='')