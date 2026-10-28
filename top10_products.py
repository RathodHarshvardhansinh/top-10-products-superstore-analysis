"""
Task 19 - Top 10 Products by Sales (Superstore dataset)

Usage:
    python top10_products.py
    python top10_products.py --input data/Sample-Superstore.csv --top 10

Outputs (in ./output):
    top10_products.csv    - Top-10 table
    top10_products.xlsx   - Top-10 table in Excel
    top10_products.png    - Bar chart
"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def load_data(path: Path) -> pd.DataFrame:
    """Load the Superstore CSV (it is usually latin-1 encoded)."""
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not read {path} with a supported encoding.")


def top_products(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Aggregate sales per product and return the top n (sorted descending)."""
    agg = (
        df.groupby("Product Name", as_index=False)
        .agg(Total_Sales=("Sales", "sum"), Quantity=("Quantity", "sum"))
        .sort_values("Total_Sales", ascending=False)
        .reset_index(drop=True)
    )
    agg["Total_Sales"] = agg["Total_Sales"].round(2)
    agg["Rank"] = agg["Total_Sales"].rank(method="min", ascending=False).astype(int)
    return agg, agg.head(n).copy()


def check_ties(full: pd.DataFrame, n: int) -> None:
    """Report whether a tie exists at the Top-N cutoff."""
    if len(full) <= n:
        print("Fewer products than N - no cutoff tie possible.")
        return
    nth, next_ = full.loc[n - 1, "Total_Sales"], full.loc[n, "Total_Sales"]
    if nth == next_:
        tied = full[full["Total_Sales"] == nth]["Product Name"].tolist()
        print(f"TIE at cutoff (sales = {nth}): {tied}")
    else:
        print(f"No tie at the cutoff (#{n} = {nth}, #{n + 1} = {next_}).")


def plot(top: pd.DataFrame, out: Path) -> None:
    data = top.sort_values("Total_Sales")  # smallest at bottom
    labels = [p if len(p) <= 40 else p[:37] + "..." for p in data["Product Name"]]
    fig, ax = plt.subplots(figsize=(11, 6))
    bars = ax.barh(labels, data["Total_Sales"], color="#f97316")
    ax.set_title("Top 10 Products by Sales (Superstore)", fontsize=14, weight="bold")
    ax.set_xlabel("Total Sales ($)")
    for bar in bars:
        ax.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            f" {bar.get_width():,.0f}",
            va="center",
            fontsize=9,
        )
    ax.margins(x=0.12)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Top N products by sales")
    parser.add_argument("--input", default="data/Sample-Superstore.csv")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)

    df = load_data(Path(args.input))
    full, top = top_products(df, args.top)
    check_ties(full, args.top)

    top_out = top[["Rank", "Product Name", "Total_Sales", "Quantity"]]
    top_out.to_csv(out_dir / "top10_products.csv", index=False)
    top_out.to_excel(out_dir / "top10_products.xlsx", index=False)
    plot(top_out, out_dir / "top10_products.png")

    print(top_out.to_string(index=False))
    print(f"\nSaved results to {out_dir.resolve()}")


if __name__ == "__main__":
    main()
