def reverse_words(s):
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start -= 1
            end -= 1

    start = end = 0
    while end >= 0:
        end = s.find(b' ', start)
        reverse_range(s, start, end-1)
        start = end + 1

    reverse_range(s, start, len(s)-1)
