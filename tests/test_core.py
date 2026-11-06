from pathlib import Path

import pytest

from csv_names import CsvNamesError, iter_names, read_rows
from csv_names.cli import main

SAMPLE = Path(__file__).parent / "sample.csv"


def test_read_rows_keys():
    rows = list(read_rows(SAMPLE))
    assert rows[0]["email"] == "spresnail0@angelfire.com"


def test_iter_names():
    assert list(iter_names(SAMPLE))[0] == ("Sigfried", "Presnail")


def test_missing_file():
    with pytest.raises(CsvNamesError):
        list(read_rows("nope.csv"))


def test_missing_column():
    with pytest.raises(CsvNamesError, match="available"):
        list(iter_names(SAMPLE, first_col="nope"))


def test_cli_text(capsys):
    assert main([str(SAMPLE)]) == 0
    assert capsys.readouterr().out.splitlines()[0] == "Sigfried Presnail"


def test_cli_error(capsys):
    assert main(["nope.csv"]) == 1
    assert "error:" in capsys.readouterr().err
