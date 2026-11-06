# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`csv-names` is a zero-runtime-dependency Python library plus CLI (`csv-names`) for reading people records from CSV files. It is a practice project for agentic AI with Claude; AI-agent features are planned but not yet present. Remote: `kishancloudeng/csv-names` (public). No LICENSE by design.

## Commands

Set up (editable install with dev tools):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

- Test all: `pytest`
- Single test: `pytest tests/test_core.py::test_missing_column`
- Lint: `ruff check .` (rules `E,F,I,B` are pinned in `pyproject.toml`; keep them, an unpinned ruff picks up stricter user-level config)
- Run CLI: `csv-names examples/people.csv [--first-col X --last-col Y --format json]`
- Run example: `python examples/basic_usage.py`

CI (`.github/workflows/ci.yml`) runs `ruff check .` and `pytest` on Python 3.9–3.13, so code must stay **Python 3.9 compatible** (use `typing.Dict/Tuple/Optional/Union`, not `dict[...]`/`X | Y` syntax at runtime).

## Architecture

`src/` layout, package `csv_names`:

- `core.py` — all data logic. `read_rows(path)` is the base generator (dict per row); `iter_names` builds on it. Both are lazy generators and raise `CsvNamesError` (the only custom exception) for unreadable file, missing header, or missing column. **No printing or `sys.exit` here**; callers decide what to do with data.
- `cli.py` — thin argparse wrapper over `core`. `main(argv) -> int` returns an exit code (0 ok, 1 on `CsvNamesError`, message to stderr) instead of exiting, so tests call it directly. Registered as the `csv-names` console script in `pyproject.toml`.
- `__init__.py` — defines the public API (`__all__`) and `__version__`. Version is duplicated in `pyproject.toml`; bump both and add a `CHANGELOG.md` entry.

Because `read_rows` is a generator, errors (including a missing file) surface on first iteration, not at call time; tests wrap calls in `list(...)` for this reason.

## Data and tests

- `examples/people.csv` — 1000 rows of generated fake data (`id,first_name,last_name,email,gender,ip_address`).
- `tests/sample.csv` — 5-row fixture (first row: Sigfried Presnail) that tests assert against; don't reorder it.

## Gotchas

- Packaging uses setuptools via `pyproject.toml` only (no `setup.py`). Editable installs need pip >= 21.3 — upgrade pip in old venvs.
- The sibling dir `GIT_krs891/agentic_ai/` is the original pre-rename scratch script; this repo supersedes it.
