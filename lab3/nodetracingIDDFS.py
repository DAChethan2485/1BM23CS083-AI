def dls(node, target, depth, tree, visited):
    if depth < 0:
        return False
    visited.append(node)
    if node == target:
        return True
    if node not in tree:
        return False
    for child in tree[node]:
        if dls(child, target, depth - 1, tree, visited):
            return True
    return False

def iddfs(root, target, max_depth, tree):
    visited = []
    for depth in range(max_depth + 1):
        if dls(root, target, depth, tree, visited):
            break
    return visited

# Define the tree
tree = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': ['h', 'i']    
}

# Run IDDFS
trace = iddfs('a', 'g', 4, tree)
print("Traversal path to 'g':", trace)
