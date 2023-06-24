stack=[]
def push():
    element=int(input("Enter the element:"))
    stack.append(element)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed Element:",e)
def display():
    print(stack)
def peek():
    if not stack:
        print("Stack is empty")
    else:
        print(stack.pop())
        print(stack[len(stack)-1])
while True:
    print("Select operation 1.push 2.pop 3.display 4.peek 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("Enter correct choice")