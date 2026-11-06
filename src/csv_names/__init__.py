"""csv-names: read people records from CSV files."""

from .core import CsvNamesError, iter_names, read_rows

__version__ = "0.1.0"
__all__ = ["CsvNamesError", "iter_names", "read_rows", "__version__"]
