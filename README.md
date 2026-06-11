# Autonomous Supply Chain Disruption Monitoring Agent

A multi-agent Generative AI system that monitors global news for supply chain
disruptions, maps the impact to suppliers in a mock multi-tier supply chain,
and generates an actionable mitigation plan.

## Project Overview

- **Risk Manager Agent**: Scores severity of news (Natural Disaster, Labor Strike, Safe, etc.)
- **Network Visualizer Agent**: Maps disruptions to affected suppliers using a mock supply chain graph
- **Alternative Sourcing Agent**: Recommends backup vendors

## Tech Stack
- Python
- CrewAI / LangGraph for agent orchestration
- Tavily / DuckDuckGo Search for news
- NetworkX for supply chain graph modeling
- Pydantic for structured outputs

## Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd supply-chain-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Project Structure

```
supply-chain-agent/
├── data/              # Mock supply chain data, news samples
├── src/
│   ├── scraper/       # News fetching (Tavily/DuckDuckGo)
│   ├── agents/         # Risk Manager, Network Visualizer, Sourcing agents
│   ├── graph/          # NetworkX supply chain graph logic
│   └── reports/        # JSON -> Markdown/HTML report generation
└── tests/             # Unit tests
```

## Team

| Member | Role |
|---|---|
| Lead | Risk Manager Agent + Orchestration |
| Member 2 | News Ingestion (Search/Scraping) |
| Member 3 | Supply Chain Graph + Network Visualizer Agent |
| Member 4 | Sourcing Agent + Report Generation |

## Roadmap

- **Week 1**: News search integration + disruption classification
- **Week 2**: Mock supply chain knowledge graph
- **Week 3**: Multi-agent architecture (CrewAI/LangGraph)
- **Week 4**: Structured reporting + final UI
