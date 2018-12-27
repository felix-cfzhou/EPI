# replace occurrences of punctuation with their string names
def replace(s):
    ps = set((',', '.', '?', '!'))
    translations = {
            ',': "COMMA",
            '.': "DOT",
            '?': "QUESTION MARK",
            '!': "EXCLAMATION MARK"}
    c = collections.Counter(ch for ch in s if ch in ps)
    N = len(s)
    final_size = N
    for k in c:
        final_size += c[k]*(len(translations[k]) - 1)
    s.extend([""] * (final_size-N))
    write_ind = final_size - 1
    for i in range(N-1, -1, -1):
        if s[i] in ps:
            trans = translations[s[i]]
            s[write_ind-len(trans):write_ind+1] = trans
            write_ind -= len(trans)
        else:
            s[write_ind] = s[i]
            write_ind -= 1
