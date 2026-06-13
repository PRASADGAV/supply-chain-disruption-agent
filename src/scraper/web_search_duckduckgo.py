"""
web_search_duckduckgo.py
Day 2: Added function to fetch news for multiple queries and save to JSON.
"""

import json
import time
from ddgs import DDGS


def search_news(query: str, max_results: int = 5):
    results = []
    ddgs = DDGS()
    for r in ddgs.news(query, max_results=max_results):
        results.append({
            "title": r.get("title"),
            "body": r.get("body"),
            "url": r.get("url"),
            "source": r.get("source"),
            "date": r.get("date"),
        })
    return results


def fetch_all_news(queries: list, max_results: int = 3) -> list:
    """Fetch news for multiple queries and combine into one list."""
    all_articles = []
    for q in queries:
        articles = search_news(q, max_results=max_results)
        all_articles.extend(articles)
        time.sleep(2)  # avoid rate limiting between queries
    return all_articles


def save_to_json(articles: list, filepath: str = "../../data/raw_news.json"):
    import os
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} articles to {filepath}")


if __name__ == "__main__":
    queries = [
        "port strike supply chain",
        "semiconductor shortage",
        "shipping container delay",
        "factory fire manufacturing",
    ]
    articles = fetch_all_news(queries)
    save_to_json(articles)
