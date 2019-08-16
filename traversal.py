class traverse:
        def __init__(self , key):
            self.left = None
            self.right = None
            self.key  = key

def Preorder(T):
    if T:
        print(T.key),

        print(Preorder(T.left))

        print(Preorder(T.right))

def Inorder(T):
    if T:
        print(Inorder(T.left))

        print(T.key),

        print(Inorder(T.right))

def Postorder(T):
    if T:
        print(Postorder(T.left))

        print(Postorder(T.right))

        print(T.key),


T = traverse(1)
T.left = traverse(2)
T.right = traverse(3)
T.left.left = traverse(4)
T.left.right = traverse(5)
print('Preorder: ')
print(Preorder(T))
print('Inorder: ')
Inorder(T)
print('Postorder: ')
Postorder(T)
