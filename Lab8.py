import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

G.add_nodes_from([
    "Computer","Monitor","CPU","Hardware"
])

isa=[
    ("Monitor","Hardware"),
    ("CPU","Hardware"),
    ("Monitor","Hardware")
]

hasa=[
    ("Computer","Monitor"),
    ("Computer","CPU")
]

for a,b in isa:
    G.add_edge(a,b,relation='is-a')
for a,b in hasa:
    G.add_edge(a,b,relation='has-a')

pos=nx.spring_layout(G)

nx.draw(G,pos,with_labels=True,node_size=1500,node_color='lightblue',arrows=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,"relation"))

plt.show()