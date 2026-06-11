"""
news_fetcher.py
Fetches recent logistics/supply-chain news articles.

Day 1 version: uses duckduckgo-search (free, no API key needed)
so the team can get started immediately. Tavily integration
can be added later once the API key is set up (see .env.example).
"""

from duckduckgo_search import DDGS


def fetch_news(query: str = "global supply chain disruption", max_results: int = 5):
    """
    Fetch recent news articles related to the query.

    Args:
        query: search query string
        max_results: number of articles to fetch

    Returns:
        List of dicts with 'title', 'body', 'url'
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "body": r.get("body"),
                "url": r.get("url"),
                "date": r.get("date"),
            })
    return results


if __name__ == "__main__":
    articles = fetch_news()
    for i, article in enumerate(articles, start=1):
        print(f"\n--- Article {i} ---")
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Date: {article['date']}")
