# Customer Call List – Data Cleaning Project Usibg Pandas

## Overview

This project demonstrates the process of cleaning and standardizing a raw customer dataset in **Microsoft Excel**. The goal was to transform an inconsistent, error-prone spreadsheet into a clean, structured, analysis-ready dataset.

## Objective

Raw business data is rarely ready for analysis. This project simulates a real-world scenario where a customer call list contains typos, inconsistent formatting, duplicate records, and unnecessary columns — and walks through the steps taken to clean it.

## Tools Used

- Microsoft Excel
- Excel Tables & Filters
- Text Functions (`TRIM`, `SUBSTITUTE`, `LEFT`, `RIGHT`, `MID`)
- Find & Replace
- Data Validation

## Cleaning Steps Performed

1. **Removed extra characters** — Fixed names containing stray symbols (e.g. `/White`, `...Potter`).
2. **Standardized phone numbers** — Converted inconsistent formats (`123/643/9775`, `7066950392`) into a single uniform format (`XXX-XXX-XXXX`).
3. **Standardized categorical values** — Unified inconsistent entries like `Y`, `N`, `Yes`, `No` into a single consistent Yes/No format.
4. **Split combined data into separate columns** — Broke the single `Address` field into Street Name, State, and Zip Code.
5. **Removed duplicate records.**
6. **Removed irrelevant columns** (e.g. `Not_Useful_Column`).
7. **Applied consistent formatting** — Excel Tables with header filters for a clean, filterable layout.

## Result

A properly structured dataset where every column has a consistent format, address data is split into usable fields, duplicates and irrelevant data are removed, and the sheet is filter- and analysis-ready.

## Files in this Repository

| File | Description |
|---|---|
| `Customer Call List.xlsx` | Original raw dataset |
| `Cleaned .xlsx` | Final cleaned dataset |

## Note on Scope

This project was completed entirely in Excel. A pandas-based version of the same cleaning workflow is planned as a follow-up to demonstrate the equivalent process in Python.

## Key Takeaway

This project highlights core data cleaning skills essential for any data analyst — standardization, deduplication, restructuring, and formatting — which form the foundation for reliable data analysis.

## Data Source

Exercise dataset from **Alex the Analyst** — [YouTube](https://www.youtube.com/@AlexTheAnalyst). Cleaning steps and Excel implementation completed independently.

## Author

**Muhammad Usman**
Data Analytics Student | Aspiring Data Analyst
[LinkedIn](https://www.linkedin.com/in/muhammad-usman-332988310)
