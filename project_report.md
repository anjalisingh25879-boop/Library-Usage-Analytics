# Library Usage Analytics — Project Report

## 1. Introduction
Libraries generate circulation data every time books are borrowed and returned. Analyzing this data helps librarians understand demand, improve collection planning, identify active member groups, and monitor borrowing behavior.

## 2. Problem Statement
Manual inspection of circulation records makes it difficult to identify long-term trends, highly demanded categories, active members, and late-return patterns. This project converts circulation records into measurable KPIs and interactive visualizations.

## 3. Objectives
- Analyze book circulation.
- Compare book categories.
- Study member borrowing behavior.
- Identify monthly borrowing trends.
- Find frequently borrowed books.
- Measure borrowing duration and late-return rate.

## 4. Methodology
The project uses a synthetic CSV dataset containing 20 transactions. Python/Pandas is used for data loading, grouping, aggregation and KPI calculation. Plotly and Streamlit provide interactive visualization and filtering. IBM Bob is used as the AI-assisted development environment for generating, reviewing, improving and documenting the software project.

## 5. Key KPIs
- Total borrowings
- Unique books circulated
- Active members
- Average borrowing duration
- Late-return rate
- Most borrowed category
- Most active member type

## 6. Expected Outcome
The dashboard provides a simple view of circulation demand and borrowing behavior. Library staff can use the results to plan acquisitions, identify popular subject areas, understand member needs, and improve return management.

## 7. Conclusion
The Library Usage Analytics project demonstrates how structured data analysis can turn routine circulation records into useful operational insights. The application is intentionally modular so that real library data can replace the demonstration dataset without changing the overall dashboard concept.
