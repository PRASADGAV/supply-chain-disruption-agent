"""
supply_chain_graph.py
Day 2: Builds a NetworkX directed graph from the mock supply chain JSON.
Each node = a supplier/facility. Edges = dependency relationships.
"""

import json
import networkx as nx


def load_supply_chain(filepath: str = "data/supply_chain.json") -> dict:
    with open(filepath, "r") as f:
        return json.load(f)


def build_graph(data: dict) -> nx.DiGraph:
    G = nx.DiGraph()

    all_entities = (
        data.get("tier_1_final_assembly", [])
        + data.get("tier_2_suppliers", [])
        + data.get("tier_3_raw_materials", [])
    )

    # Add nodes
    for entity in all_entities:
        G.add_node(
            entity["id"],
            name=entity["name"],
            location=entity["location"],
            part=entity.get("part", "N/A"),
        )

    # Add edges (dependency -> dependent)
    for entity in all_entities:
        for dep in entity.get("depends_on", []):
            G.add_edge(dep, entity["id"])

    return G


if __name__ == "__main__":
    data = load_supply_chain()
    G = build_graph(data)

    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")