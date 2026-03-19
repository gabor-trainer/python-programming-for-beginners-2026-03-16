

"""
Matching Pennies - Prediction Algorithm
----------------------------------------
Two players each think Heads or Tails.
- If they MATCH  → Player 1 (you) gets a point.
- If DIFFERENT   → Player 2 (algorithm) gets a point.

The algorithm predicts your next move by tracking what you
tend to pick after every 3-move sequence in history.
"""

import random

HISTORY_LEN = 100  # how many past moves to use as pattern key


def predict(table: dict, history: list) -> str:
    """Predict the human's next move using the frequency table."""
    if len(history) < HISTORY_LEN:
        return random.choice(["H", "T"])

    key = "".join(history[-HISTORY_LEN:])
    if key not in table:
        return random.choice(["H", "T"])

    counts = table[key]
    if counts["H"] == counts["T"]:
        return random.choice(["H", "T"])

    return "H" if counts["H"] > counts["T"] else "T"


def update_table(table: dict, history: list, choice: str):
    """Record what the human picked after the last HISTORY_LEN moves."""
    if len(history) < HISTORY_LEN:
        return
    key = "".join(history[-HISTORY_LEN:])
    if key not in table:
        table[key] = {"H": 0, "T": 0}
    table[key][choice] += 1


def get_input() -> str:
    """Prompt the human for H or T."""
    while True:
        try:
            raw = input(
                "  Your pick — [H]eads or [T]ails (or Q to quit): ").strip().upper()
        except EOFError:
            return "Q"
        if raw in ("H", "T", "Q"):
            return raw
        print("  Please enter H, T, or Q.")


def show_scores(you: int, ai: int, rounds: int):
    print(f"\n  Score after {rounds} round(s):  You {you}  |  Algorithm {ai}")


def show_confidence(table: dict, history: list):
    """Show how confident the algorithm is about the current pattern."""
    if len(history) < HISTORY_LEN:
        print("  Algorithm: still learning your patterns...\n")
        return

    key = "".join(history[-HISTORY_LEN:])
    if key not in table:
        print("  Algorithm: no data yet for this pattern.\n")
        return

    counts = table[key]
    total = counts["H"] + counts["T"]
    if total == 0:
        return

    dominant = "H" if counts["H"] >= counts["T"] else "T"
    conf = max(counts["H"], counts["T"]) / total * 100
    print(f"  Algorithm: after [{key}] you picked "
          f"H={counts['H']}x / T={counts['T']}x "
          f"→ predicting {'Heads' if dominant == 'H' else 'Tails'} "
          f"({conf:.0f}% confidence)\n")


def play():
    history: list[str] = []
    table: dict = {}
    scores = {"you": 0, "ai": 0}
    rounds = 0

    print("=" * 50)
    print("   MATCHING PENNIES  —  vs. the Algorithm")
    print("=" * 50)
    print("  Rules:")
    print("   • If you MATCH the algorithm → YOU score.")
    print("   • If DIFFERENT              → ALGORITHM scores.")
    print("  The algorithm learns your patterns and predicts you.")
    print("  Enter Q at any time to quit.\n")

    while True:
        # show_confidence(table, history)

        choice = get_input()
        if choice == "Q":
            break

        # algorithm predicts BEFORE we update the table
        ai_pick = predict(table, history)

        # now update the table with what the human actually picked
        update_table(table, history, choice)
        history.append(choice)

        rounds += 1
        matched = choice == ai_pick

        print(f"\n  You: {'Heads' if choice == 'H' else 'Tails':<6}  "
              f"Algorithm: {'Heads' if ai_pick == 'H' else 'Tails':<6}  "
              f"→  {'MATCH — you score! ✓' if matched else 'MISMATCH — algorithm scores.'}")

        if matched:
            scores["you"] += 1
        else:
            scores["ai"] += 1

        show_scores(scores["you"], scores["ai"], rounds)

    # --- final summary ---
    print("\n" + "=" * 50)
    print("  FINAL RESULTS")
    print("=" * 50)
    show_scores(scores["you"], scores["ai"], rounds)

    if rounds > 0:
        ai_win_pct = scores["ai"] / rounds * 100
        print(f"  Algorithm win rate: {ai_win_pct:.1f}%  "
              f"(expected ~50% vs. a truly random player)")
        if ai_win_pct > 55:
            print("  The algorithm found your patterns. Try being more random!")
        elif ai_win_pct < 45:
            print("  You beat the algorithm — impressive randomness!")
        else:
            print("  Roughly even — you were hard to predict.")

    print("\n  Patterns learned:")
    if table:
        for key, counts in sorted(table.items()):
            total = counts["H"] + counts["T"]
            bar_h = "#" * counts["H"]
            bar_t = "#" * counts["T"]
            print(f"    [{key}] → H: {bar_h:<10} {counts['H']}   "
                  f"T: {bar_t:<10} {counts['T']}   (total: {total})")
    else:
        print("    (not enough rounds to build a table)")

    print("=" * 50)


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\n\n  Game interrupted. Goodbye!")
    except Exception as e:
        print(f"\n  An unexpected error occurred: {e}")
