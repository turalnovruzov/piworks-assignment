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
    elif n % 2 == 0 or n % 3 == 0:
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

def preorder_traversal(tree: list, i: int, sum_: int, max_: int):
    sum_ += tree[i]
    max_ = max(max_, sum_)

    left_child = i*2
    right_child = i*2 + 1

    if left_child < len(tree):
        max_ = preorder_traversal(tree, left_child, sum_, max_)
    if right_child < len(tree):
        max_ = preorder_traversal(tree, right_child, sum_, max_)
    
    return max_

def find_sum(tree: list) -> int:
    return preorder_traversal(tree, 1, 0, 0)

# I will store the pyramid in a binary tree structure.
# Since the binary tree given to me is a perfect binary tree, I wil store it as a list.
tree = [-1]

# Read the pyramid and store it in the tree list
with open('input.txt') as f:
    for line in f:
        numbers = [int(x) for x in line.strip().split()]
        tree.extend(numbers)
print(tree)
print(find_sum(tree))

