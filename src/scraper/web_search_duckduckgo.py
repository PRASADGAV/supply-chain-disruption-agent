"""
web_search_duckduckgo.py
Fetches recent news using ddgs (formerly duckduckgo-search, free, no API key).
"""

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


if __name__ == "__main__":
    queries = [
        "port strike supply chain",
        "semiconductor shortage",
        "shipping delay",
    ]
    for q in queries:
        print(f"\n=== Query: {q} ===")
        for article in search_news(q, max_results=3):
            print(f"- {article['title']} ({article['source']})")
        time.sleep(2)  # avoid rate limiting between queries
