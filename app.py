
import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Library Usage Analytics", page_icon="📚", layout="wide")
DATA = Path(__file__).resolve().parents[1] / "data" / "library_circulation.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA, parse_dates=["borrow_date", "due_date", "return_date"])
    df["month"] = df["borrow_date"].dt.to_period("M").astype(str)
    return df

df = load_data()

st.title("📚 Library Usage Analytics")
st.caption("Book circulation, categories, members and borrowing trends")

with st.sidebar:
    st.header("Filters")
    cats = st.multiselect("Book category", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
    members = st.multiselect("Member type", sorted(df["member_type"].unique()), default=sorted(df["member_type"].unique()))
    date_range = st.date_input("Borrowing date", [df["borrow_date"].min().date(), df["borrow_date"].max().date()])

filtered = df[
    df["category"].isin(cats) &
    df["member_type"].isin(members) &
    (df["borrow_date"].dt.date >= date_range[0]) &
    (df["borrow_date"].dt.date <= date_range[1])
]

total_borrows = len(filtered)
unique_books = filtered["book_id"].nunique()
unique_members = filtered["member_id"].nunique()
late_rate = (filtered["return_status"].eq("Late").mean() * 100) if len(filtered) else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Borrowings", f"{total_borrows:,}")
c2.metric("Unique Books", f"{unique_books:,}")
c3.metric("Active Members", f"{unique_members:,}")
c4.metric("Late Return Rate", f"{late_rate:.1f}%")

left, right = st.columns(2)

monthly = filtered.groupby("month").size().reset_index(name="borrowings")
left.plotly_chart(px.line(monthly, x="month", y="borrowings", markers=True, title="Monthly Borrowing Trend"),
                  use_container_width=True)

cat = filtered.groupby("category").size().reset_index(name="borrowings").sort_values("borrowings", ascending=False)
right.plotly_chart(px.bar(cat, x="category", y="borrowings", title="Borrowings by Category"),
                   use_container_width=True)

left, right = st.columns(2)
mt = filtered.groupby("member_type").size().reset_index(name="borrowings")
left.plotly_chart(px.pie(mt, names="member_type", values="borrowings", title="Borrowings by Member Type"),
                  use_container_width=True)

avg_days = filtered.groupby("category")["days_borrowed"].mean().reset_index()
right.plotly_chart(px.bar(avg_days, x="category", y="days_borrowed", title="Average Borrowing Duration"),
                   use_container_width=True)

st.subheader("Most Borrowed Books")
top_books = filtered.groupby("book_id").size().reset_index(name="borrowings").sort_values("borrowings", ascending=False).head(10)
st.dataframe(top_books, use_container_width=True, hide_index=True)

st.subheader("Key Insights")
if len(cat):
    top_category = cat.iloc[0]["category"]
    top_member = mt.sort_values("borrowings", ascending=False).iloc[0]["member_type"]
    st.write(f"- **Most popular category:** {top_category}.")
    st.write(f"- **Most active member group:** {top_member}.")
    st.write(f"- **Late-return rate:** {late_rate:.1f}% of filtered transactions.")
    st.write("- Use the filters to compare categories, member groups and time periods.")
