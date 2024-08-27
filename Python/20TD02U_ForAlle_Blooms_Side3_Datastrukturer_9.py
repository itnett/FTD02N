python
def dfs(graf, start, besøkt=None):
    if besøkt is None:
        besøkt = set()
    besøkt.add(start)
    print(start)
    for nabo in graf[start]:
        if nabo not in besøkt:
            dfs(graf, nabo, besøkt)

# Bruk av DFS
graf = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
dfs(graf, "A")