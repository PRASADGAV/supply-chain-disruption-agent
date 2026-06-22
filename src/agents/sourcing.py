"""
sourcing.py
Day 2: Initial rule-based logic for suggesting alternative suppliers.
This will later be wrapped in an Alternative Sourcing Agent (Week 3).
"""

import json
from src.agents.schemas import SourcingRecommendation

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

def get_sourcing_recommendation(
    data: dict, part: str, disrupted_id: str
) -> SourcingRecommendation:
    """Find alternatives and return a validated Pydantic SourcingRecommendation."""
    alternatives = find_alternatives(data, part, disrupted_id)
    alt_ids = [a["id"] for a in alternatives]

    recommendation = SourcingRecommendation(
        part=part,
        primary_supplier_id=disrupted_id,
        alternative_supplier_ids=alt_ids,
        notes=f"Found {len(alt_ids)} alternative(s) for {part}"
    )
    return recommendation

if __name__ == "__main__":
    data = load_supply_chain()

    rec = get_sourcing_recommendation(
        data,
        "Microcontroller Unit",
        "TIER2-CHIP-01"
    )

    print(rec.model_dump())