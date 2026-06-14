"""
schemas.py
Pydantic models defining the structured output contracts
for the Risk Manager, Network Visualizer, and Sourcing agents.
These will be refined as agent logic is built in Week 3-4.
"""

from pydantic import BaseModel, Field
from typing import List, Literal


class RiskAssessment(BaseModel):
    headline: str
    category: Literal["Natural Disaster", "Labor Strike", "Geopolitical", "Safe", "Other"]
    severity: Literal["Low", "Medium", "High", "Critical"]
    affected_region: str
    summary: str = Field(..., description="1-2 sentence summary of the disruption")


class ImpactedSupplier(BaseModel):
    supplier_id: str
    supplier_name: str
    tier: int
    part_affected: str


class NetworkImpactReport(BaseModel):
    risk: RiskAssessment
    impacted_suppliers: List[ImpactedSupplier]


class SourcingRecommendation(BaseModel):
    part: str
    primary_supplier_id: str
    alternative_supplier_ids: List[str]
    notes: str


class DisruptionActionPlan(BaseModel):
    risk: RiskAssessment
    network_impact: NetworkImpactReport
    sourcing: List[SourcingRecommendation]