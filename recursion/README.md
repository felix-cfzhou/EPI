# Recursion

- excellent if the input is expressed in recursive definitions
- good for search, enumeration, divide-and-conquer
- use recursion as an alternative ot deeply nested iteration loops
    - better for undefined number of levels
- to remove recursion, consider mimicking call stacks with the stack data structure
- tail-recursive programs can be removed using a while-loop
- consider caching the results if the recursive function ends up being called with the same arguments more than once
