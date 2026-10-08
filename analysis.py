
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "library_circulation.csv"
OUT = Path(__file__).resolve().parents[1] / "reports"
df = pd.read_csv(DATA, parse_dates=["borrow_date", "due_date", "return_date"])

monthly = df.groupby(df["borrow_date"].dt.to_period("M")).size().reset_index(name="borrowings")
monthly["month"] = monthly["borrow_date"].astype(str)
monthly.drop(columns=["borrow_date"]).to_csv(OUT / "monthly_borrowing_trend.csv", index=False)

category = df.groupby("category").agg(
    borrowings=("transaction_id","count"),
    unique_books=("book_id","nunique"),
    avg_days_borrowed=("days_borrowed","mean")
).sort_values("borrowings", ascending=False)
category.to_csv(OUT / "category_analysis.csv")

members = df.groupby("member_type").agg(
    borrowings=("transaction_id","count"),
    unique_members=("member_id","nunique"),
    avg_days_borrowed=("days_borrowed","mean")
).sort_values("borrowings", ascending=False)
members.to_csv(OUT / "member_analysis.csv")

top_books = df.groupby("book_id").size().reset_index(name="borrowings").sort_values("borrowings", ascending=False).head(20)
top_books.to_csv(OUT / "top_books.csv", index=False)

summary = {
    "total_transactions": len(df),
    "unique_books": df["book_id"].nunique(),
    "unique_members": df["member_id"].nunique(),
    "late_return_rate_percent": round((df["return_status"].eq("Late").mean()*100), 2),
    "average_days_borrowed": round(df["days_borrowed"].mean(), 2),
}
pd.DataFrame([summary]).to_csv(OUT / "kpi_summary.csv", index=False)
print(summary)
