# Brute force method is to traverse one node upwards and keeping track of path with a hashtable

# We save space by starting a dual traversal from the same level
# O(h) time h is height, O(1) space
def lca(node_0, node_1):
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        depth_diff -= 1
        node_0 = node_0.parent
    
    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent
    return node_0
