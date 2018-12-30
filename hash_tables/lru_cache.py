class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._isbn_price_table = collections.OrderedDict()

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)  # moves the price to front of queue
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price
    
    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None
