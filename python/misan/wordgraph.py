def wordgraph(words, edges):
    outputs = []
    graph = {}
    for i in range(ord('a'), ord('z')+1):
        graph[chr(i)] = []
    for edge in edges:
        fromword = edge[0]
        toword = edge[1]
        graph[fromword].append(toword)
    for word in words:
        outputs.append(is_spelled(word, graph))
    return outputs

def is_spelled(word, graph):
    for i in range(len(word)-1):
        c = word[i]
        c1 = word[i+1]
        if c1 not in graph[c]:
            return 0
    return 1

if __name__ == '__main__':
    print wordgraph(['a','b','ab','ba'],[('a','b')])
    print wordgraph(['a','b','ab','ba','be','abc','ace','cea'],[('a','b'),('a','c'),('b','d'),('c','e')])
    print wordgraph(['a','b','ab','ba'],[('a','b')])
