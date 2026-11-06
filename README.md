# csv-names

A small Python library and command-line tool for reading people records (first/last name, email, etc.) from CSV files. Zero runtime dependencies, Python 3.9+.

## Install

```bash
pip install git+https://github.com/kishancloudeng/csv-names.git
# or for development
git clone https://github.com/kishancloudeng/csv-names.git && cd csv-names
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## CLI

```console
$ csv-names examples/people.csv
Sigfried Presnail
Rhetta Haquin
...
$ csv-names data.csv --first-col given --last-col family --format json
```

| Option | Default | Meaning |
|---|---|---|
| `--first-col` | `first_name` | header of the first-name column |
| `--last-col` | `last_name` | header of the last-name column |
| `--format` | `text` | `text` or `json` |
| `--version` | | print version |

Exit code is `0` on success and `1` on error (message goes to stderr).

## Library

```python
from csv_names import iter_names, read_rows, CsvNamesError

for first, last in iter_names("examples/people.csv"):
    print(first, last)

for row in read_rows("examples/people.csv"):   # dict per row
    print(row["email"])
```

- `read_rows(path)` yields `dict[str, str]` per row.
- `iter_names(path, first_col="first_name", last_col="last_name")` yields `(first, last)` tuples.
- Both raise `CsvNamesError` for a missing/unreadable file, empty file, or missing column.
- Files must be UTF-8 with a header row. Fully type-hinted (`py.typed`).

## Development

```bash
pytest        # run tests
ruff check .  # lint
```

`examples/people.csv` is 1000 rows of generated fake data (columns `id,first_name,last_name,email,gender,ip_address`).

## Roadmap
AI-agent features are planned (this repo is a practice project for agentic AI with Claude).
