# Hash Tables

- hash tables have best theoretical and real-world performance for:
    - lookup
    - insert
    - delete
- considering using a hash code as a signature to enhance performance
    - ie filter out candidates
- consider a precomputed lookup table instead of boilerplate id-then code for mappings
- understand the relationship between logical equality and the fields the hash function must inspect
- we may sometimes need a multimap or a bidirectional map
    - multimap using lists as values
    - third party library which includes multimap

## An implementation suitable for strings

```python3
def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)
```

```python3
class ContactList:
    def __init__(self, names):
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)

    def merge_contact_lists(contacts):
        return list(set(contacts))
```

## Hash Table Libraries

```python3
set
s = set()
t = set()
s.add(e)
s.remove(e)
s.discard(e)
x in s
s <= t  # subset
s - t  # elements of s not in t

dict

collections.defaultdict
d = collections.defaultdict(list)
if k not in d:
    d[k] == []

collections.Counter
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
c + d
c - d
c & d  # min
c | d  # max
```
