import networkx as nx
from .sample_data import get_sample_ore


def build_graph():
    data = get_sample_ore()

    G = nx.DiGraph()

    for edge in data:
        G.add_node(edge["source"],label=edge["source"])
        G.add_node(edge["target"],label=edge["target"])

        G.add_edge(
            edge["source"],
            edge["target"],
            relation=edge["relation"]
        )
    
    return G


