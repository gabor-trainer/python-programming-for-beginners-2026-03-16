# ADR 002: Selection of Python Tooling and Package Management

## Status
Decided (2026-02-17)

## Context
Python projects require a way to manage external libraries (like `requests`) and isolated environments (Virtual Environments) to prevent version conflicts between different projects on the same machine.

Historically, the standard was using `venv` and `pip` with a `requirements.txt` file. However, this process is manual, relatively slow, and does not provide "lockfiles" by default for reproducible builds.

## Decision
We have decided to use **`uv`** by Astral for project management.

### Why `uv`?
*   **Performance:** Written in Rust, it is 10-100x faster than `pip` and `poetry`.
*   **Unified Tooling:** It replaces `pip`, `venv`, `pip-tools`, and even manages Python versions. This reduces the number of tools a developer needs to learn.
*   **Reproducibility:** It automatically generates a `uv.lock` file. This ensures that every developer on the team uses the exact same version of every library, down to the last byte.
*   **Modern Standards:** It uses `pyproject.toml`, which is the current PEP-compliant standard for Python project configuration.

## Alternatives Considered
1.  **`pip` + `venv`:** The "classic" approach. Rejected because it is slower, requires manual activation of environments, and doesn't easily track dependencies in a structured way without extra steps.
2.  **Poetry:** A very popular "all-in-one" tool. Rejected because it is significantly slower than `uv` and has a steeper learning curve for simple projects.
3.  **Conda:** Rejected as it is too "heavy" for a simple API-based script and is better suited for Data Science/Machine Learning workloads with complex C-dependencies.

## Consequences

### Pros
*   **Speed:** Installing new packages or setting up the project on a new machine is nearly instantaneous.
*   **Simplified Workflow:** Using `uv run main.py` automatically handles environment activation, so the developer doesn't have to remember to "source" or "activate" the virtual environment manually.
*   **Self-Correction:** `uv` handles common errors (like the `hardlink` warning we saw) gracefully by falling back to safe defaults.

### Cons
*   **Newer Tool:** `uv` is relatively new (released in 2024), so it might have fewer stack-overflow answers compared to `pip`.
*   **Installation Step:** Requires a one-time global installation of `uv` on the developer's machine.

## Implementation Details
*   **Lockfile:** `uv.lock` is committed to the repository to guarantee identical environments.
*   **Execution:** The project is run via `uv run`, ensuring the correct virtual environment is always used.

---

### Which one should you prioritize?
In a professional portfolio, having **these two ADRs** (API Choice + Tooling Choice) shows that you aren't just "writing code," but you are **thinking like an engineer** who evaluates trade-offs.

Would you like to add a third one regarding the **Coding Standards (PEP 8 & English only)**, or are you ready to add some more features to the code?