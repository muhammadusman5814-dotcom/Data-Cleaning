# Customer Call List – Data Cleaning Project (Pandas)

## Overview

This project demonstrates cleaning and standardizing a raw customer dataset using **Python (pandas)**. The goal was to transform an inconsistent, error-prone spreadsheet into a clean, structured, analysis-ready dataset.

## Objective

Raw business data is rarely ready for analysis. This project simulates a real-world scenario where a customer call list contains typos, inconsistent formatting, duplicate records, and unnecessary columns — and walks through the pandas code used to clean it.

## Tools Used

- Python
- pandas
- Regular expressions (`re`, via `str.replace(..., regex=True)`)

## Cleaning Steps Performed

1. **Loaded the raw dataset** with `pd.read_excel()`.
2. **Removed duplicate rows** with `drop_duplicates()`.
3. **Cleaned `Last_Name`** — stripped stray characters from the ends of each value.
4. **Standardized `Phone_Number`** — removed all non-alphanumeric characters via regex, reformatted every value into a consistent `XXX-XXX-XXX` pattern, and cleaned up leftover "nan"/"Na" artifacts from missing entries.
5. **Split `Address` into separate columns** — used `str.split(',', expand=True)` to break the combined field into `Street Name`, `State`, and `Zip Code`.
6. **Standardized `Paying Customer` and `Do_Not_Contact`** — normalized inconsistent `Y`/`N`/`N/a` entries into a consistent `Yes`/`No` format, including follow-up passes to fix edge cases introduced by the initial replace (e.g. "Yeses", "Noo").
7. **Handled missing values** — filled remaining blanks with `fillna("")`.
8. **Removed rows with no usable phone number** — dropped any row where `Phone_Number` ended up empty, then reset the index.
9. **Exported the cleaned dataset** with `df.to_excel()`.

## Result

A structured dataset where phone numbers, address fields, and Yes/No columns follow consistent formats, duplicates are removed, and rows with no usable contact number are dropped.

## Known Limitations

- `Not_Useful_Column` is normalized (`TRUE`/`FALSE` → `True`/`False`) but not dropped from the final output — a planned follow-up is to drop it explicitly with `df.drop(columns=['Not_Useful_Column'])`.
- The `Last_Name` cleaning step uses `.str.strip()` with a character set intended as a regex pattern; `.strip()` doesn't interpret regex, so it strips any of those literal characters from the ends of the string rather than matching the intended pattern. It works on this dataset but would need `str.replace(..., regex=True)` to behave as originally intended on messier data.

## Files in this Repository

| File | Description |
|---|---|
| `Customer Call List.xlsx` | Original raw dataset |
| `Data Cleaning.py` | Pandas script performing the cleaning |
| `Cleaned .xlsx` | Final cleaned dataset, exported from the script |

## Key Takeaway

This project highlights core data cleaning skills essential for any data analyst — deduplication, regex-based text standardization, column splitting, and handling messy/missing values — using pandas.

## Data Source

Exercise dataset from **Alex the Analyst** — [YouTube](https://www.youtube.com/@AlexTheAnalyst). Cleaning script written independently.

## Author

**Muhammad Usman**
Data Analytics Student | Aspiring Data Analyst
[LinkedIn](https://www.linkedin.com/in/muhammad-usman-332988310)
