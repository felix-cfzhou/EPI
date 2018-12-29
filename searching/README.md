# Searching

- we initially focus on static data stored in sorted order in an array
- binary search can be used for more than just sorted arrays
    - search an interval of real numbers or integers
- If the solution uses sorting and the computation performed after sorting is faster than sorting, consider solutions which do not performa a complete sort
- consider time / space tradeoffs
    - making multiple passes through the data

## Canonical Examples

```python3
# Binary Search O(log n) time
def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L)//2
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1
```

```python3
# binary search a custom comparator comparing HI-LO GPA and ties broken by name
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)

def search_student(students, target, comp_gpa):
    return 0 <= i < len(students) and students[i] == target
```

## Libraries

- `bisect` library
- `bisect.bisect_left(a, x)` finds the indec of the first element that is not less than a targeted value else `len(a)`
- `bisect.bisect_right(a, x)` is similar but for the first element that is greater than the targeted value

