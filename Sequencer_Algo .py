# sequencer.py
from datetime import date
from typing import Any

def existing_rows_by_date(sheet, headers_len: int) -> dict[date, list[Any]]:
    """
    Harvests all existing logs from the spreadsheet 
    into an in-memory dictionary keyed by trading date.
    """
    rows = {}
    max_column = max(sheet.max_column, headers_len)
    
    for row_cells in sheet.iter_rows(min_row=3, max_row=sheet.max_row, min_col=1, max_col=max_column, values_only=True):
        if not row_cells or row_cells[0] is None:
            continue
        row_date = row_cells[0] 
        if isinstance(row_date, date):
            rows[row_date] = list(row_cells)
    return rows


def write_rows_sorted(sheet, rows_by_date: dict[date, list[Any]], headers_len: int) -> None:
    """
    Clears out physical rows and completely rewrites them 
    in sorted, flawless chronological order.
    """
    if sheet.max_row >= 3:
        sheet.delete_rows(3, sheet.max_row - 2)

    for row_number, row_date in enumerate(sorted(rows_by_date), start=3):
        values = rows_by_date[row_date]
        
        
        if len(values) < headers_len:
            values = values + [None] * (headers_len - len(values))
        values[9] = row_number - 2
        for column, value in enumerate(values, start=1):
            sheet.cell(row=row_number, column=column).value = value