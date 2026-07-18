# Customer Call List – Excel Data Cleaning Project

## 📌 Overview
This project demonstrates the process of cleaning and standardizing a raw customer dataset in **Microsoft Excel**. The goal was to transform an inconsistent, error-prone spreadsheet into a clean, structured, and analysis-ready dataset.

## 🎯 Objective
Raw business data is rarely ready for analysis. This project simulates a real-world scenario where a customer call list contains typos, inconsistent formatting, duplicate records, and unnecessary columns — and walks through the steps taken to clean it.

## 🛠️ Tools Used
- Microsoft Excel
- Excel Tables & Filters
- Text Functions (`TRIM`, `SUBSTITUTE`, `LEFT`, `RIGHT`, `MID`)
- Find & Replace
- Data Validation

## 🔧 Cleaning Steps Performed
1. **Removed extra characters** — Fixed names containing stray symbols (e.g. `/White`, `...Potter`).
2. **Standardized phone numbers** — Converted inconsistent formats (`123/643/9775`, `7066950392`) into a single, uniform format (`XXX-XXX-XXXX`).
3. **Standardized categorical values** — Unified inconsistent entries like `Y`, `N`, `Yes`, `No` into a single consistent Yes/No format.
4. **Split combined data into separate columns** — Broke the single `Address` field into **Street Name**, **State**, and **Zip Code** for easier filtering and analysis.
5. **Removed duplicate records** — Identified and deleted a duplicate customer entry.
6. **Removed irrelevant columns** — Dropped columns that added no analytical value (e.g. `Not_Useful_Column`).
7. **Applied consistent formatting** — Used Excel Tables with header filters for a clean, presentable, and functional layout.

## ✅ Result
A properly structured dataset where:
- Every column has a consistent, single format
- Address data is split into usable fields (Street, State, Zip Code)
- Duplicate and irrelevant data has been removed
- The sheet is filter- and analysis-ready

## 📂 Files in this Repository
| File | Description |
|------|-------------|
| `before.xlsx` / screenshot | Original raw dataset |
| `after.xlsx` / screenshot | Final cleaned dataset |

## 📈 Key Takeaway
This project highlights core **data cleaning** skills essential for any data analyst — including standardization, deduplication, restructuring, and formatting — which form the foundation for accurate and reliable data analysis.

## 👤 Author
**Muhammad Usman**
Data Analytics Student | Aspiring Data Analyst
[LinkedIn](#) • [GitHub](#)
