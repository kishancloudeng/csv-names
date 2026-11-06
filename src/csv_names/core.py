"""Core CSV reading functions. No printing happens here; callers decide what to do with data."""

import csv
from pathlib import Path
from typing import Dict, Iterator, Tuple, Union

PathLike = Union[str, Path]


class CsvNamesError(Exception):
    """Raised for unreadable files or missing columns."""


def read_rows(path: PathLike) -> Iterator[Dict[str, str]]:
    """Yield each CSV row as a dict keyed by the header names.

    Args:
        path: Path to a UTF-8 CSV file with a header row.

    Raises:
        CsvNamesError: If the file does not exist or has no header.
    """
    p = Path(path)
    try:
        f = open(p, newline="", encoding="utf-8")
    except OSError as e:
        raise CsvNamesError(f"Cannot read {p}: {e.strerror}") from e
    with f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise CsvNamesError(f"{p} is empty or has no header row")
        yield from reader


def iter_names(
    path: PathLike,
    first_col: str = "first_name",
    last_col: str = "last_name",
) -> Iterator[Tuple[str, str]]:
    """Yield ``(first_name, last_name)`` for each row.

    Args:
        path: Path to the CSV file.
        first_col: Header of the first-name column.
        last_col: Header of the last-name column.

    Raises:
        CsvNamesError: If either column is missing from the file.
    """
    for row in read_rows(path):
        try:
            yield row[first_col], row[last_col]
        except KeyError as e:
            raise CsvNamesError(
                f"Column {e.args[0]!r} not found; available: {', '.join(row)}"
            ) from e
