"""
One-time (or occasional refresh) script that scrapes the demo regulatory
documents via the Apify `apify/rag-web-browser` actor and saves them as
markdown files in corpus/. Run locally — never from Streamlit Cloud.

Usage:
    python scripts/build_corpus.py
"""
import os
import re
import time
from pathlib import Path
from datetime import datetime, timezone

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

CORPUS_DIR = Path(__file__).parent.parent / "corpus"
MAX_DOC_CHARS = 8000  # cap per scraped page to keep total corpus manageable

QUERIES = [
    "RBI master direction IT framework banks cybersecurity",
    "CERT-In directions 2025 breach notification 6 hours India",
    "DPDP Act 2023 rules compliance India cross-border transfer",
    "RBI data localization payment systems circular India",
    "RBI cloud computing framework 2024 banks outsourcing",
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def main():
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("APIFY_API_TOKEN is not set. Add it to .env first.")

    CORPUS_DIR.mkdir(exist_ok=True)
    client = ApifyClient(token)

    doc_count = 0
    for query in QUERIES:
        print(f"Scraping: {query}")
        try:
            run = client.actor("apify/rag-web-browser").call(
                run_input={
                    "query": query,
                    "maxResults": 3,
                    "outputFormats": ["markdown"],
                }
            )
        except Exception as e:
            print(f"  Failed to run actor for '{query}': {e}")
            continue

        items = client.dataset(run["defaultDatasetId"]).list_items().items
        for i, item in enumerate(items):
            markdown = (item.get("markdown") or "").strip()
            url = item.get("url", "unknown-source")
            if not markdown:
                continue

            doc_count += 1
            filename = f"{slugify(query)}-{i}.md"
            frontmatter = (
                f"---\n"
                f"source_url: {url}\n"
                f"query: {query}\n"
                f"scraped_at: {datetime.now(timezone.utc).isoformat()}\n"
                f"---\n\n"
            )
            content = frontmatter + markdown[:MAX_DOC_CHARS]

            with open(CORPUS_DIR / filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Saved {filename} ({len(content)} chars)")

        time.sleep(1)  # be polite between actor calls

    print(f"\nDone. {doc_count} documents saved to {CORPUS_DIR}/")
    print("Commit these files to git so Streamlit Cloud can load them without Apify access.")


if __name__ == "__main__":
    main()
