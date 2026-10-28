# Top 10 Products by Sales – Superstore Analysis

**Veda Technology · Data Analytics Internship · Task 19 (Level 1, Day 19)**

Identify the top 10 products by total sales in the Superstore dataset, practicing ranking and sorting with Python (pandas) and Excel.

## Objective

Practice ranking and sorting: aggregate sales per product, sort descending, check for ties at the cutoff, and visualise the result.

## Tools

- Python (pandas, matplotlib, openpyxl)
- Excel (output workbook)

## Dataset

Superstore sales dataset (`Sample-Superstore.csv`). Place it in the `data/` folder. Required columns: `Product Name`, `Sales`, `Quantity`.

## Project Structure

```
top-10-products-superstore-analysis/
├── data/
│   └── Sample-Superstore.csv     # add dataset here
├── output/                        # generated results
│   ├── top10_products.csv
│   ├── top10_products.xlsx
│   └── top10_products.png
├── top10_products.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python top10_products.py
# optional
python top10_products.py --input data/Sample-Superstore.csv --top 10
```

## Approach

1. Load the CSV (tries utf-8, then latin-1 / cp1252).
2. Group by `Product Name`, summing `Sales` and `Quantity`.
3. Sort by total sales in descending order and assign a rank.
4. Check for ties at the Top-10 cutoff (rank 10 vs rank 11).
5. Export the Top-10 table to CSV and Excel, and plot a horizontal bar chart.

## Deliverables

- **Top-10 table** – `output/top10_products.csv` and `output/top10_products.xlsx`
- **Chart** – `output/top10_products.png`

## Hints Applied

- Sort descending before taking the top N.
- Ties are checked at the cutoff and reported in the console.

## Interview Questions

**How do you handle ties?**
Rank with `method="min"` so tied products share a rank, and compare the Nth and (N+1)th values. If they are equal, report all tied products (or state the tie-break rule, e.g. by quantity).

**Why use Top 10 analysis?**
It focuses attention on the few products driving most revenue (Pareto principle), guiding inventory, marketing and pricing decisions.

## Results

After running the script, add your chart here:

```
![Top 10 Products](output/top10_products.png)
```

## Author

Rathod Harshvardhansinh J – Data Analytics Intern, Veda Technology
