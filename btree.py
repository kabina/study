class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.depth = 0

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    # def depth(self):
    #     l = self.left.depth() if self.left else 0
    #     r = self.right.depth() if self.right else 0
    #
    #     if l > r :
    #         return l + 1
    #     else:
    #         return r +1

n1 = Node(4)
n2 = Node(3)
n3 = Node(2)
n4 = Node(20)
n5 = Node(50)
n6 = Node(60)
n7 = Node(30)
n8 = Node(40)

n1.left = n2
n1.right = n3
n2.right = n5
n2.left = n4
n4.left = n7
n4.right = n8
n3.right = n6

def set_depth(node, depth):
    node.depth += depth + 1
    if node.left :
        set_depth(node.left, node.depth)
    if node.right :
        set_depth(node.right, node.depth)

def pre_order(node):
    print(node.name, end=" ")
    if node.left :
        pre_order(node.left)
    if node.right :
        pre_order(node.right)

def in_order(node):
    if node.left :
        in_order(node.left)
    print(node.name, end=" ")
    if node.right :
        in_order(node.right)

def post_order(node):
    if node.left :
        post_order(node.left)
    if node.right :
        post_order(node.right)
    print(node.name, end=" ")

height = 0
def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right))+1

def root_find(node):
    if node.left :
        root_find(node.left)
    if node.right :
        root_find(node.right)
    if node.left is None and node.right is None:
        print(node.name)

height = height(n1)

depth = 0
def dep(node):
    global depth
    depth += 1
    if node.left == None and node.right == None :
        return 0
    elif node.left == None :
        return dep(node.right)
    elif node.right == None :
        return dep(node.left)
    else:
        return max(dep(node.left), dep(node.right))+1

#print(height(n1))
#print(dep(n1))

#post_order(n1)
#print(n2.depth())

def last_node(node):
    global depth
    if node == None:
        return


    if height == depth :
        print(node.name, end=" ")
    if node.left or node.right :
        depth += 1

    if node.left :
        last_node(node.left)
    if node.right :
        last_node(node.right)

set_depth(n1, 0)

# print("="*20)
# post_order(n1)

root_find(n1)