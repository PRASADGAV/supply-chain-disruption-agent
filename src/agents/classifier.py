"""
classifier.py
Day 2: Uses Groq (free, fast inference) to classify a news article
into a disruption category.
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

CLASSIFICATION_PROMPT = """You are a supply chain risk analyst.
Classify the following news article into ONE category:
- "Natural Disaster"
- "Labor Strike"
- "Geopolitical"
- "Safe" (if no supply chain relevance)

Also provide a severity: "Low", "Medium", "High", "Critical".

Respond ONLY with valid JSON in this exact format, nothing else:
{{"category": "...", "severity": "...", "summary": "one sentence summary"}}

Article Title: {title}
Article Body: {body}
"""


def classify_article(title: str, body: str) -> dict:
    prompt = CLASSIFICATION_PROMPT.format(title=title, body=body)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    content = response.choices[0].message.content.strip()

    # Strip markdown code fences if the model adds them
    if content.startswith("```"):
        content = content.strip("`").replace("json\n", "").strip()

    return json.loads(content)


if __name__ == "__main__":
    sample_title = "Major Port Strike Halts Shipments at Los Angeles Port"
    sample_body = "Dockworkers at the Port of Los Angeles began a strike today, halting all container operations."
    result = classify_article(sample_title, sample_body)
    print(result)