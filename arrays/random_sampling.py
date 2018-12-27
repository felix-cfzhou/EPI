# get a random subset of size k O(n) time
def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
