# Dynamic Programming

- find a way to break the problem into subproblems such that
    - the original problem can be solved easily once solutions to the subproblems are available
    - these subproblem solutions are cached
- consider DP when we make choices to arrive at the solution
    - when we can construct a solution to the given instance from solutions to subinstances of smaller problems of the same kind
- DP is applicable to counting and decision making problems
- for efficiency, consider building the DP cache iteratively
- recursive implementations use hash tables and BSTs while iterative solutions use arrays
- consider recycling cache space once it is known that a set of entries will not be looked up again
- recursion may out-perform an iterative solutions if the solution is found early or subproblems can be pruned through bounding
- do not always attempt to divide the problem in half
    - it is often insufficient
- DP is based on combining solutions to subproblems to yield a solution to the original problem
    - may not be suitable for all problems
