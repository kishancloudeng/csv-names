"""Run from the repo root: python examples/basic_usage.py"""
from pathlib import Path

from csv_names import iter_names

for first, last in list(iter_names(Path(__file__).parent / "people.csv"))[:5]:
    print(first, last)
