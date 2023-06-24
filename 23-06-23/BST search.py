class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def search(root,key):
    #Base cases:root is null or key is present or not
    if root is None or root.val==key:
        return root
    # key value greater than roots key
    if root.val<key:
        return search(root.right,key)
    # key is smaller than roots key
    return search(root.left,key)
r=Node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
inorder(r)
key=int(input("Enter value to be searched:"))
if search(r,key):
    print("Element found")
else:
    print("Element not found")
search(r,key)
