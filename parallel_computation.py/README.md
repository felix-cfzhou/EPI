# Parallel Computation

- consider starting an algorithm that locks aggressively and is easily seen to be correct, then add back concurrency, while ensuring the critical parts are locked
- when analyzing

## Benefits

- high performance
    - more processors working on a task
- better use of resources
- fairness
    - users / programs share a machine
- convenience
    - more straightforward to complete task using a set of concurrent programs for subtasks rather than having a single program manage all subtasks
- fault tolerance
    - if a machine fails in a cluster, others can take over

## Examples

- graphical user interfaces (GUI)
    - different threads for different tasks
        - UI
        - communication
- Java Virtual Machines
    - seperate thread for garbage collection
- web servers
    - one logical thread per client request
- scientific computing
    - matrix multiplication
- web search
    - multiple machines for:
        - crawling
        - indexing
        - retrieving web pages

## Models of Parallel Computation

### Shared Memory Model

- each processor can access any location in memory
- more appropriate for multicore settings

### Distributed Memory Model

- a processor must explicitly send a message to another processor to access its memory
- more appropriate for clusters

## Challenges

Difficulties arise due to subtle interactions between parallel components.

Debugging may be difficult as bugs are usually load dependent and not reproducible.

Also, a task may be blocked by something which cannot be parallelized.

- races
    - two concurrent instruction sequences access the same address in memory
    - at least one of them writes to that address
- starvation
    - processor needs a resource but never gets it
- deadlock
    - thread `A` acquires Lock `L1`, `B` acquires `L2`
    - `A` tries to acquire `L2`, `B` tries to acquire `L1` 
- livelock
    - processor keeps retrying an operation that always fails
