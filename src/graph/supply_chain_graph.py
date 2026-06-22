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

    for entity in all_entities:
        G.add_node(
            entity["id"],
            name=entity["name"],
            location=entity["location"],
            part=entity.get("part", "N/A"),
        )

    for entity in all_entities:
        for dep in entity.get("depends_on", []):
            G.add_edge(dep, entity["id"])

    return G


def find_suppliers_by_location(G: nx.DiGraph, location_keyword: str) -> list:
    matches = []
    for node, attrs in G.nodes(data=True):
        if location_keyword.lower() in attrs.get("location", "").lower():
            matches.append({"id": node, **attrs})
    return matches


def find_downstream_impact(G: nx.DiGraph, node_id: str) -> list:
    return list(nx.descendants(G, node_id))


if __name__ == "__main__":
    data = load_supply_chain()
    G = build_graph(data)

    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    taiwan_suppliers = find_suppliers_by_location(G, "Taiwan")
    print("\nSuppliers in Taiwan:", taiwan_suppliers)

    if taiwan_suppliers:
        node_id = taiwan_suppliers[0]["id"]
        impact = find_downstream_impact(G, node_id)
        print(f"\nIf {node_id} is disrupted, downstream impact on:", impact)