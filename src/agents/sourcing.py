"""
sourcing.py
Day 2: Initial rule-based logic for suggesting alternative suppliers.
This will later be wrapped in an Alternative Sourcing Agent (Week 3).
"""

import json


def load_supply_chain(filepath: str = "data/supply_chain.json") -> dict:
    with open(filepath, "r") as f:
        return json.load(f)


def find_alternatives(data: dict, part: str, exclude_id: str) -> list:
    """
    Find suppliers in tier_2 or tier_3 that produce the same part,
    excluding the disrupted supplier.
    """
    alternatives = []
    all_suppliers = data.get("tier_2_suppliers", []) + data.get("tier_3_raw_materials", [])

    for supplier in all_suppliers:
        if supplier.get("part") == part and supplier["id"] != exclude_id:
            alternatives.append(supplier)

    return alternatives


if __name__ == "__main__":
    data = load_supply_chain()

    # Example: TIER2-CHIP-01 (Taiwan) is disrupted, find alternatives for "Microcontroller Unit"
    disrupted_id = "TIER2-CHIP-01"
    part = "Microcontroller Unit"

    alternatives = find_alternatives(data, part, disrupted_id)

    if alternatives:
        print(f"Alternatives for {part} (excluding {disrupted_id}):")
        for alt in alternatives:
            print(f"- {alt['name']} ({alt['location']})")
    else:
        print(f"No alternatives found for {part}. Need to expand mock data with backup suppliers.")