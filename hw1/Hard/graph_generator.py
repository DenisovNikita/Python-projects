import pygraphviz as pgv

G = pgv.AGraph(directed=True)

# G.graph_attr["label"] = "Name of graph"
G.node_attr["shape"] = "circle"
# G.node_attr["color"] = "red"

G.add_node("A", color="red")
G.add_edge("A", "B")

s = G.string()

G.layout(prog="dot")

G.draw("graph.png")
