import networkx as nx

def create_graph(entities):

    G = nx.Graph()

    for equipment in entities["equipment"]:
        G.add_node(equipment)

    for issue in entities["issues"]:
        for equipment in entities["equipment"]:
            G.add_edge(equipment, issue)

    for engineer in entities["engineers"]:
        for equipment in entities["equipment"]:
            G.add_edge(engineer, equipment)

    return G