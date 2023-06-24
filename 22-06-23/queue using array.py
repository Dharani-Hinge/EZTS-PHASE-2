queue=[]
def enqueue():
    element=input("Enter element")
    queue.append(element)
    print(element,"is added in queue")
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop(0)
        print("Removed Element",e)
def display():
    print(queue)
while True:
    print("Select operation 1.add 2.remove 3.show 4.quit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct choice")