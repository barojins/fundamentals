# Task 1 Report: Package and Linear Core Patterns

## Implementation details

Added the `python.dsa` package and standalone `python.dsa.core` module. The core module implements the requested active-recall patterns: frequency counting, sorted two-sum, fixed-window maximum, longest unique substring, prefix sums and range queries, Kadane maximum subarray, binary search, lower bound, monotonic-stack next greater values, interval merging, and heap-backed top-k selection.

Each function has a five-line memory card describing when to use it, prerequisites, invariant, reconstruction cue, and complexity. Required standard-library imports are present; unused imports required by the brief are explicitly marked for Ruff and Pyright.

Added the requested package/test marker docstrings and the three focused unit tests covering core behavior and preconditions.

## Files changed

- `python/dsa/__init__.py`
- `python/dsa/core.py`
- `python/tests/__init__.py`
- `python/tests/dsa/__init__.py`
- `python/tests/dsa/test_core.py`

Existing `python/quick_templates.py`, `python/templates.py`, and `python/concise_templates.py` were not changed.

## TDD evidence

### RED

Command:

```text
uv run python -m unittest python/tests/dsa/test_core.py
```

Result: failed during test import with `ModuleNotFoundError: No module named 'python.dsa.core'`, as expected before implementation.

### GREEN

Commands:

```text
uv run python -m unittest python/tests/dsa/test_core.py
uv run ruff check python/dsa/core.py python/tests/dsa/test_core.py
uv run ruff format --check python/dsa/core.py python/tests/dsa/test_core.py
uv run pyright python/dsa/core.py python/tests/dsa/test_core.py
```

Results:

```text
Ran 3 tests in 0.000s
OK
All checks passed!
2 files already formatted
0 errors, 0 warnings, 0 informations
```

Repository-wide discovery was also run once before commit:

```text
uv run python -m unittest discover -s python -p 'test*.py'
```

Result: `Ran 13 tests in 0.000s` / `OK`.

## Self-review

- Verified all 12 requested public functions and their specified edge-case errors.
- Verified sorted search assumptions, inclusive range-sum indexing, strict next-greater behavior, touching interval merging, and descending top-k output.
- Confirmed focused Ruff, format, and Pyright checks pass.
- Confirmed the full existing Python test suite passes.
- Confirmed only the five requested new files are in the commit.

## Concerns

- The brief requires importing `deque`, `heappop`, `heappush`, and `count` even though Task 1 does not use them; targeted Ruff/Pyright suppressions preserve those required imports without quality-check failures.
- The repository-wide `check.py` has known unrelated Ruff failures in `python/concise_templates.py`; no repo-wide `check.py` result was used as evidence for this scoped deliverable.

## Commit

`fe5c3c0 feat: add linear DSA core templates`
