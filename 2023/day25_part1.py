import itertools
import sys
from collections import Counter
from functools import cmp_to_key
from itertools import cycle
from itertools import repeat
from itertools import chain
from itertools import islice
from heapq import *
from collections import deque
from collections import defaultdict
from copy import deepcopy

'''
Put that in an online python runner with networkx installed
See: https://trinket.io/embed/python3/a5bd54189b
def print_minimum_edge_cut(lines):
    import networkx as nx
    G = nx.Graph()
    for line in lines:
        key, tokens = line.split(':')
        for token in tokens.split():
            G.add_edge(key, token)
            G.add_edge(token, key)
    print(G.minimum_edge_cut())
'''

def process_all(lines):
    graph = defaultdict(set)
    candidates = set()

    for line in lines:
        key, tokens = line.split(':')
        for token in tokens.split():
            graph[key].add(token)
            graph[token].add(key)

    for key, links in graph.items():
        if key in ['nmz', 'vgf', 'fdb']:
            for n in links:
                if (n, key) not in candidates:
                    candidates.add((key, n))
                    # displayed in graphviz to filter candidates. Online graphviz: https://www.devtoolsdaily.com/graphviz/?#v2=N4IgJg9gLiBcIgL5A
                    print(key, '->', n)

    def is_in_same_graph(node1, node2, cuts):
        open_set = [node1]
        closed_set = set()
        while open_set:
            node = open_set.pop(0)
            if node in closed_set:
                continue
            closed_set.add(node)

            if node == node2:
                return True

            for n in graph[node]:
                if (node, n) not in cuts and (n, node) not in cuts:
                    open_set.append(n)

        return False

    def get_size(node, cuts):
        open_set = [node]
        closed_set = set()
        while open_set:
            node = open_set.pop(0)
            if node in closed_set:
                continue
            closed_set.add(node)

            for n in graph[node]:
                if (node, n) not in cuts and (n, node) not in cuts:
                    open_set.append(n)

        return len(closed_set)

    def solve():
        print('Nb candidates', len(candidates))
        for cut1, cut2, cut3 in itertools.combinations(candidates, 3):
            node1, node2 = cut1
            cuts = set()
            cuts.add(cut1)
            cuts.add(cut2)
            cuts.add(cut3)
            if not is_in_same_graph(node1, node2, cuts):
                return get_size(node1, cuts) * get_size(node2, cuts)

    print(graph)
    # print(candidates)
    return solve()


input = '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''

lines = list(input.splitlines()[1:])

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
