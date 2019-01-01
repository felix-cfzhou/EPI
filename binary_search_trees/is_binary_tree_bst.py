def is_binary_tree_bst(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    bfs_queue = collections.deque([QueueEntry(tree, float('inf'), float('inf'))])
    
    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                    QueueEntry(front.node.left, front.lower, front.node.data),
                    QueueEntry(front.node.right, front.data, front.upper)]
    return True

