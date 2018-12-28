def sort_approximately_sorted_array(sequence, k):
    sequence = iter(sequence)
    result = []
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    return result
