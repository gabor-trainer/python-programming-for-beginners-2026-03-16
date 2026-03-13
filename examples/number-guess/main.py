"""
Number Guessing Game — Tkinter Edition
Functional, event-driven, rich UI with guess history,
color-coded feedback, animated progress bar, and replay.
"""

import random
import tkinter as tk
from tkinter import font as tkfont

# ── Palette ──────────────────────────────────────────────
BG = "#1a1b26"   # dark indigo
PANEL = "#24283b"   # card bg
ACCENT = "#7aa2f7"   # soft blue
ACCENT_DIM = "#3d59a1"
SUCCESS = "#9ece6a"   # green
WARNING = "#e0af68"   # amber
DANGER = "#f7768e"   # coral-red
TEXT = "#c0caf5"   # light lavender
TEXT_DIM = "#565f89"
ENTRY_BG = "#1a1b26"
BORDER = "#414868"

MAX_GUESSES = 7
LO, HI = 1, 50

# ── State (module-level dict so closures can mutate it) ──
state = {}


def new_game_state():
    return dict(
        secret=random.randint(LO, HI),
        attempts=0,
        history=[],       # list of (guess, result_text, color)
        game_over=False,
        won=False,
    )


# ── UI construction ──────────────────────────────────────

def build_ui(root):
    root.title("Guess the Number")
    root.configure(bg=BG)
    root.resizable(False, False)

    # Fonts
    title_font = tkfont.Font(family="Helvetica Neue", size=22, weight="bold")
    sub_font = tkfont.Font(family="Helvetica Neue", size=11)
    entry_font = tkfont.Font(family="Courier", size=20, weight="bold")
    btn_font = tkfont.Font(family="Helvetica Neue", size=12, weight="bold")
    hist_font = tkfont.Font(family="Courier", size=11)
    hint_font = tkfont.Font(family="Helvetica Neue", size=13, weight="bold")

    # ── Main frame ───────────────────────────────────────
    frame = tk.Frame(root, bg=BG, padx=32, pady=24)
    frame.pack(fill="both", expand=True)

    # Title
    tk.Label(
        frame, text="🎯  Guess the Number", font=title_font,
        bg=BG, fg=ACCENT
    ).pack(anchor="w")

    tk.Label(
        frame, text=f"I'm thinking of a number between {LO} and {HI}. You get {MAX_GUESSES} tries.",
        font=sub_font, bg=BG, fg=TEXT_DIM
    ).pack(anchor="w", pady=(2, 16))

    # ── Progress bar ─────────────────────────────────────
    prog_frame = tk.Frame(frame, bg=BG)
    prog_frame.pack(fill="x", pady=(0, 16))

    pip_labels = []
    for i in range(MAX_GUESSES):
        pip = tk.Frame(prog_frame, width=40, height=6, bg=BORDER)
        pip.pack(side="left", padx=(0, 6))
        pip.pack_propagate(False)
        pip_labels.append(pip)

    remaining_var = tk.StringVar(value=f"{MAX_GUESSES} guesses remaining")
    tk.Label(
        prog_frame, textvariable=remaining_var, font=sub_font,
        bg=BG, fg=TEXT_DIM
    ).pack(side="right")

    # ── Input row ────────────────────────────────────────
    input_frame = tk.Frame(frame, bg=BG)
    input_frame.pack(fill="x", pady=(0, 8))

    entry_var = tk.StringVar()
    entry = tk.Entry(
        input_frame, textvariable=entry_var, font=entry_font,
        bg=ENTRY_BG, fg=TEXT, insertbackground=ACCENT,
        relief="flat", width=6, justify="center",
        highlightthickness=2, highlightbackground=BORDER,
        highlightcolor=ACCENT
    )
    entry.pack(side="left", ipady=6)
    entry.focus_set()

    guess_btn = tk.Button(
        input_frame, text="Guess", font=btn_font,
        bg=ACCENT, fg=BG, activebackground=ACCENT_DIM,
        activeforeground=TEXT, relief="flat", padx=20, pady=6,
        cursor="hand2"
    )
    guess_btn.pack(side="left", padx=(12, 0))

    # ── Feedback label ───────────────────────────────────
    feedback_var = tk.StringVar(value="")
    feedback_label = tk.Label(
        frame, textvariable=feedback_var, font=hint_font,
        bg=BG, fg=TEXT, anchor="w"
    )
    feedback_label.pack(fill="x", pady=(8, 4))

    # ── History panel ────────────────────────────────────
    hist_outer = tk.Frame(frame, bg=BORDER, bd=0)
    hist_outer.pack(fill="both", expand=True, pady=(8, 0))

    tk.Label(
        hist_outer, text="  HISTORY", font=sub_font,
        bg=PANEL, fg=TEXT_DIM, anchor="w"
    ).pack(fill="x", ipady=4)

    hist_canvas = tk.Canvas(hist_outer, bg=PANEL,
                            highlightthickness=0, height=170)
    hist_scrollbar = tk.Scrollbar(
        hist_outer, orient="vertical", command=hist_canvas.yview)
    hist_inner = tk.Frame(hist_canvas, bg=PANEL)

    hist_inner.bind(
        "<Configure>",
        lambda e: hist_canvas.configure(scrollregion=hist_canvas.bbox("all"))
    )
    hist_canvas.create_window((0, 0), window=hist_inner, anchor="nw")
    hist_canvas.configure(yscrollcommand=hist_scrollbar.set)

    hist_canvas.pack(side="left", fill="both", expand=True)
    hist_scrollbar.pack(side="right", fill="y")

    # ── Play-again button (hidden initially) ─────────────
    again_btn = tk.Button(
        frame, text="▶  Play Again", font=btn_font,
        bg=SUCCESS, fg=BG, activebackground="#7db85a",
        activeforeground=BG, relief="flat", padx=20, pady=6,
        cursor="hand2"
    )

    # ── Pack references into a dict for event handlers ───
    widgets = dict(
        root=root, entry=entry, entry_var=entry_var,
        guess_btn=guess_btn, again_btn=again_btn,
        feedback_var=feedback_var, feedback_label=feedback_label,
        remaining_var=remaining_var,
        pip_labels=pip_labels,
        hist_inner=hist_inner, hist_canvas=hist_canvas,
        hist_font=hist_font, sub_font=sub_font,
    )
    return widgets


# ── Event handlers ───────────────────────────────────────

def add_history_row(w, number, text, color):
    """Append one row to the history panel."""
    row = tk.Frame(w["hist_inner"], bg=PANEL)
    row.pack(fill="x", padx=8, pady=2)

    tk.Label(
        row, text=f" {number:>2} ", font=w["hist_font"],
        bg=PANEL, fg=TEXT, width=4
    ).pack(side="left")

    tk.Label(
        row, text=text, font=w["hist_font"],
        bg=PANEL, fg=color, anchor="w"
    ).pack(side="left", fill="x", expand=True)

    # Auto-scroll to bottom
    w["hist_canvas"].update_idletasks()
    w["hist_canvas"].yview_moveto(1.0)


def update_pips(w):
    """Color the progress pips based on attempts."""
    for i, pip in enumerate(w["pip_labels"]):
        if i < state["attempts"]:
            if state["won"] and i == state["attempts"] - 1:
                pip.configure(bg=SUCCESS)
            else:
                pip.configure(bg=WARNING if not state["game_over"] else DANGER)
        else:
            pip.configure(bg=BORDER)


def handle_guess(w):
    """Process one guess — the core event callback."""
    if state["game_over"]:
        return

    raw = w["entry_var"].get().strip()
    w["entry_var"].set("")

    # Validate
    if not raw.isdigit():
        w["feedback_var"].set("⚠  Enter a whole number")
        w["feedback_label"].configure(fg=WARNING)
        return

    guess = int(raw)
    if guess < LO or guess > HI:
        w["feedback_var"].set(f"⚠  Pick between {LO} and {HI}")
        w["feedback_label"].configure(fg=WARNING)
        return

    state["attempts"] += 1
    remaining = MAX_GUESSES - state["attempts"]

    if guess == state["secret"]:
        # ── Win ──
        state["game_over"] = True
        state["won"] = True
        label = "✓ Correct!"
        color = SUCCESS
        w["feedback_var"].set(
            f"🎉  You got it in {state['attempts']} guess{'es' if state['attempts'] != 1 else ''}!"
        )
        w["feedback_label"].configure(fg=SUCCESS)
        end_round(w)

    elif guess < state["secret"]:
        label = "↑ Too low"
        color = ACCENT
        w["feedback_var"].set(f"⬆  Too low!   ({remaining} left)")
        w["feedback_label"].configure(fg=ACCENT)

    else:
        label = "↓ Too high"
        color = DANGER
        w["feedback_var"].set(f"⬇  Too high!   ({remaining} left)")
        w["feedback_label"].configure(fg=DANGER)

    add_history_row(w, guess, label, color)
    state["history"].append((guess, label, color))
    update_pips(w)

    w["remaining_var"].set(
        f"{remaining} guess{'es' if remaining != 1 else ''} remaining"
    )

    if remaining == 0 and not state["won"]:
        # ── Loss ──
        state["game_over"] = True
        w["feedback_var"].set(
            f"💀  The number was {state['secret']}. Better luck next time!")
        w["feedback_label"].configure(fg=DANGER)
        w["remaining_var"].set("0 guesses remaining")
        end_round(w)

    w["entry"].focus_set()


def end_round(w):
    """Disable input and show the Play Again button."""
    w["entry"].configure(state="disabled")
    w["guess_btn"].configure(state="disabled")
    w["again_btn"].pack(fill="x", pady=(12, 0))


def reset_game(w):
    """Re-roll the secret, clear UI, start fresh."""
    state.update(new_game_state())

    w["entry"].configure(state="normal")
    w["guess_btn"].configure(state="normal")
    w["entry_var"].set("")
    w["feedback_var"].set("")
    w["remaining_var"].set(f"{MAX_GUESSES} guesses remaining")
    w["again_btn"].pack_forget()

    # Clear history rows
    for child in w["hist_inner"].winfo_children():
        child.destroy()

    # Reset pips
    for pip in w["pip_labels"]:
        pip.configure(bg=BORDER)

    w["entry"].focus_set()


# ── Main ─────────────────────────────────────────────────

def main():
    state.update(new_game_state())

    root = tk.Tk()
    root.geometry("420x520")
    w = build_ui(root)

    # Bind events
    w["guess_btn"].configure(command=lambda: handle_guess(w))
    w["entry"].bind("<Return>", lambda e: handle_guess(w))
    w["again_btn"].configure(command=lambda: reset_game(w))

    root.mainloop()


if __name__ == "__main__":
    main()
