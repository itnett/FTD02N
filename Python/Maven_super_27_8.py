python
    from collections import deque

    class Graf:
        def __init__(self):
            self.graf = {}

        def legg_til_kant(self, node, nabo):
            if node not in self.graf:
                self.graf[node] = []
            self.graf[node].append(nabo)

        def bfs(self, start):
            besøkt = set()
            kø = deque([start])
            besøkt.add(start)

            while kø:
                node = kø.popleft()
                print(node, end=" ")

                for nabo i self.graf[node]:
                    if nabo not in besøkt:
                        kø.append(nabo)
                        besøkt.add(nabo)