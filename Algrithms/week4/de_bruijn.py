def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i + k - 1], st[i + 1:i + k]))
        nodes.add(st[i:i + k - 1])
        nodes.add(st[i - 1:i + k])
    return nodes, edges
