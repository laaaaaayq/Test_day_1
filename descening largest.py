x=int(input("Enter the number of array elements : "))
y=int(input("Enter the number of elements to return : "))
z=list(map(int,input("Enter the elements : ").split()))
a=sorted(z,reverse=True)
s=""
for i in a[:y]:
    s+=str(i)+" "
print(s)