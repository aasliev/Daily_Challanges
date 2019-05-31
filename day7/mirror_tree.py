#we were given this part of the code
{
#Initial Template for Python 3
class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None
def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)
def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()
if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        
        root = None
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]
                
                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]
            
            child = Node(int(arr[3*j+1]))
                
            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
                
        mirror(root)
        
        inorderTraversal(root)
}
#---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
def mirror(root):
    # Code here
    if root is None:
        return
    root.left , root.right = root.right,root.left
    mirror(root.left)
    mirror(root.right)
