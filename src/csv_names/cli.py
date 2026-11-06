"""Command-line interface: ``csv-names FILE``."""

import argparse
import json
import sys
from typing import List, Optional

from . import __version__
from .core import CsvNamesError, iter_names


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="csv-names", description="Print first and last names from a CSV file."
    )
    parser.add_argument("file", help="path to a CSV file with a header row")
    parser.add_argument("--first-col", default="first_name", help="first-name column header")
    parser.add_argument("--last-col", default="last_name", help="last-name column header")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    try:
        names = list(iter_names(args.file, args.first_col, args.last_col))
    except CsvNamesError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps([{"first": first, "last": last} for first, last in names], indent=2))
    else:
        for first, last in names:
            print(first, last)
    return 0


if __name__ == "__main__":
    sys.exit(main())
