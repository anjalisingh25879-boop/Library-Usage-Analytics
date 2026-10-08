# Library Usage Analytics — IBM Bob Project

## Project Overview
This project analyzes library circulation data to understand book usage, popular categories, member activity, borrowing duration, late returns, and monthly borrowing trends.

The project is designed to be developed and maintained with **IBM Bob**, an AI software-development partner. Bob can create files, analyze the repository, generate/refactor code, run commands, and improve documentation. The analytics application itself is implemented in Python with Pandas and Streamlit.

## Objectives
1. Measure total book circulation.
2. Identify the most borrowed book categories.
3. Compare borrowing activity across member types.
4. Analyze monthly borrowing trends.
5. Identify highly circulated books.
6. Calculate average borrowing duration.
7. Monitor late-return rate.
8. Provide an interactive dashboard for filtering and exploration.

## Dataset
`data/library_circulation.csv` contains 20 synthetic circulation transactions for demonstration.

Columns:
- transaction_id
- borrow_date
- book_id
- category
- member_id
- member_type
- due_date
- return_date
- days_borrowed
- return_status

## Technologies
- IBM Bob
- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- CSV

## How to Run
```bash
pip install -r requirements.txt
streamlit run src/app.py
```

For batch analysis:
```bash
python src/analysis.py
```

## Dashboard
The dashboard contains:
- KPI cards
- Monthly borrowing trend
- Borrowings by category
- Borrowings by member type
- Average borrowing duration
- Top borrowed books
- Category/member/date filters
- Automatically generated insights

## Suggested Findings
Because the dataset is synthetic, the exact rankings are generated from a fixed random seed. The dashboard calculates the findings dynamically rather than hard-coding them.

## Future Enhancements
- Add real library-management-system data.
- Add book author/publisher fields.
- Add reservation and renewal data.
- Predict future borrowing demand.
- Add recommendation system for books.
- Connect to SQL database.
- Deploy dashboard online.

## IBM Bob Workflow
1. Open this folder in IBM Bob.
2. Use `/init` to initialize project context.
3. Ask Bob to review the dataset and source files.
4. Run the Streamlit dashboard.
5. Ask Bob to improve visualizations, add analytics, test calculations, and update documentation.

### Example Bob prompt
"Analyze this library usage analytics project. Review the CSV schema, validate all KPI calculations, improve the Streamlit dashboard, add useful visualizations for circulation trends and member behavior, and update README.md with the methodology and findings. Do not replace the existing synthetic data unless necessary."


## Beginner Dataset Note
This version intentionally contains only 20 sample transactions so that a beginner can inspect the data easily while learning the project workflow. The same dashboard can later be used with a larger dataset.
