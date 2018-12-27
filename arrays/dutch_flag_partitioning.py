# Brute Force O(n) space
def dutch_flag_partition(pivot_index, A):
    less = []
    equal = []
    greater = []
    pivot = A[pivot_index]
    for e in A:
        if e < pivot:
            less.append(e)
        else if e > pivot:
            greater.append(e)
        else:
            equal.append(e)
    ind = 0
    for e in less:
        A[ind] = e
        e += 1
    for e in equal:
        A[ind] = e
        e += 1
    for e in greater:
        A[ind] = e
        e += 1


# O(1) space, O(n^2) time
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    N = len(A)
    for i in range(N):
        for j in range(i+1, N):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in range(N-1, -1, -1):
        if A[i] < pivot:
            break
        for j in range(i-1, -1, -1):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


# O(1) space, O(n) time
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    N = len(A)
    smaller = 0
    for i in range(N):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = N-1
    for i in range(N-1, -1, -1):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


# One pass improvement
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    N = len(A)
    smaller, equal, larger = 0, 0, N
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        elif A[equal] > pivot:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        else:
            equal += 1
