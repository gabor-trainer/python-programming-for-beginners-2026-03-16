import argparse
import re
from collections import Counter

try:
    from tabulate import tabulate
except ImportError:
    raise SystemExit(
        "Missing dependency: install it with `pip install tabulate`")

STOP_WORDS = {
    # Articles
    "a", "an", "the",
    # Conjunctions
    "and", "or", "but", "if", "because", "as", "until", "while",
    "although", "though", "since", "unless",
    # Prepositions
    "of", "at", "by", "for", "with", "about", "against", "between",
    "into", "through", "during", "before", "after", "above", "below",
    "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then", "once",
    # Demonstrative / location adverbs
    "here", "there", "when", "where", "why", "how",
    # Determiners / quantifiers
    "all", "any", "both", "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very",
    # Modal / auxiliary verbs
    "can", "will", "just", "should", "now",
    "is", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing",
    "would", "could", "may", "might", "shall",
    # Personal / possessive pronouns
    "i", "me", "my", "myself",
    "we", "our", "ours", "ourselves", "us",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "they", "them", "their", "theirs", "themselves",
    # Impersonal / demonstrative pronouns
    "it", "its", "itself",
    "this", "that", "these", "those",
    # Interrogative / relative pronouns
    "what", "which", "who", "whom", "whose",
    # Other common fillers
    "also", "like", "well", "even", "get", "got", "still",
}


def analyze(text: str) -> dict:
    # 1. Line calculation (raw input) — splitlines() handles trailing newlines correctly
    total_lines = len(text.splitlines())

    # 2. Whitespace normalization
    normalized = re.sub(r"\s+", " ", text).strip()

    # 3. Character count (post-normalization)
    total_chars = len(normalized)

    # 4. Case normalization
    lowered = normalized.lower()

    # 5. Punctuation removal
    cleaned = re.sub(r"[^\w\s]", "", lowered)

    # 6. Tokenization
    tokens = cleaned.split()

    # 7. Total word count (all words, no stop-word filter)
    total_words = len(tokens)

    # 8. Stop-word filtering
    filtered = [w for w in tokens if w not in STOP_WORDS]

    # 9. Frequency analysis
    unique_words = len(set(filtered))
    top10 = Counter(filtered).most_common(10)

    return {
        "total_words": total_words,
        "total_lines": total_lines,
        "total_chars": total_chars,
        "unique_words": unique_words,
        "top10": top10,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyse word frequencies in a text file."
    )
    parser.add_argument("file", help="Path to the text file to analyse")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            text = fh.read()
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found — '{args.file}'")
    except OSError as exc:
        raise SystemExit(f"Error reading file: {exc}")

    stats = analyze(text)

    # Table A — General Statistics
    general = [
        ["Total Words",      stats["total_words"]],
        ["Total Lines",      stats["total_lines"]],
        ["Total Characters", stats["total_chars"]],
        ["Unique Words",     stats["unique_words"]],
    ]
    print("\n── General Statistics ──────────────────────────")
    print(tabulate(general, headers=[
          "Metric", "Value"], tablefmt="fancy_grid"))

    # Table B — Top 10 Frequency Analysis
    print("\n── Top 10 Words (stop words excluded) ──────────")
    if stats["top10"]:
        print(tabulate(stats["top10"], headers=[
              "Word", "Count"], tablefmt="fancy_grid"))
    else:
        print("  (no words remaining after stop-word filtering)")

    print()


if __name__ == "__main__":
    main()
