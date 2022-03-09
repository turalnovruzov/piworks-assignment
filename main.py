class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def is_prime(n: int) -> bool:
    """Checks if a number is a prime number or not.

    Args:
        n (int): the number

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n == 2 or n == 3:
        return True
    elif n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    

    # All prime numbers except 2 and 3 are of form 6k+1 or 6k-1.
    # So I am only checking to see if n is divisible by prime numbers.

    i = 5   # Prime numbers
    sep = 2 # Seperator that switches between 2 and 4

    while i * i <= n:
        if n % i == 0:
            return False
        
        i += sep
        sep = 6 - sep
    
    return True

def preorder_traversal(head: Node, sum_: int, max_: int):
    # if the number is prime stop moving forward
    if is_prime(head.value):
        return max_
    
    # Calculate the new sumn and the new maximum sum
    sum_ += head.value
    max_ = max(sum_, max_)

    # calculate the maximum of the left and right branches
    if head.left is not None:
        max_ = preorder_traversal(head.left, sum_, max_)
    if head.right is not None:
        max_ = preorder_traversal(head.right, sum_, max_)
    
    # Return the maximum sum
    return max_

def find_sum(head: Node) -> int:
    return preorder_traversal(head, 0, 0)

head = Node(0)

# Read the pyramid and store it in the tree list
with open('input.txt') as f:
    # Read the head of the tree
    head.value = int(f.readline().strip())

    # Read the rest of the nodes
    parent_nodes = [head]
    for line in f:
        nodes = [Node(int(x)) for x in line.strip().split()]

        parent_nodes[0].left = nodes[0]
        parent_nodes[0].right = nodes[1]

        for i in range(1, len(parent_nodes)):
            parent_nodes[i].left = nodes[i]
            parent_nodes[i].right = nodes[i+1]
        
        parent_nodes = nodes


print(find_sum(head))
