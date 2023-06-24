ar=list(map(int,input().split()))
ar.append(6)
print(ar)
ar.remove(2)
print(ar)
x=int(input("Enter the element to be searched:"))
if x in ar:
    print("Element found")
else:
    print("Element not found")
ar.sort()
print(ar)
print("**********************************")
l=list(map(int,input().split()))
print("1.insertion")
print("2.Deletion")
print("3.Search")
print("4.Sort")
n=int(input("Enter choice:"))
if(n==1):
    a=int(input("Enter element to be added"))
    l.append(a)
    print(l)
elif(n==2):
    b=int(input("Enetr the element to be deleted:"))
    l.remove(b)
    print(l)
elif(n==3):
    c=int(input("Enter the element to be searched:"))
    if c in l:
        print("Element found")
    else:
        print("Element not found")
elif(n==4):
    l.sort()
    print(l)