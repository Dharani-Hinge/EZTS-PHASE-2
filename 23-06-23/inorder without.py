# iterative method inorder traversal without recursion using stack
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inOrder(root):
    # set current to root of binary tree
    current=root
    stack=[]
    done=0
    while True:
        # reach the left most node of the current
        if current is not None:
    # place pointer to a tree node on the stack
    # before traversing the node's left subtree
            stack.append(current)
            current=current.left
# BackTrack from empty subtree & visit Node
# at the top of stack
#however if the stack is empty you are done
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")
# we have visited the node and its left
# subtree Now its right subtrees turn
            current=current.right
        else:
            break
    print()
#INPUT
"""constructed binary tree is
               1
              /  \
             2    3
            / \
            4  5  """
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
inOrder(root)