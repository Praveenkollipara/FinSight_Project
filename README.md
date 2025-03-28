# FinSight_Project


## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Overview](#dataset-overview)
- [Technologies Used](#technologies-used)
- [Data Cleaning & Feature Engineering](#data-cleaning-and-feature-engineering)
- [Exploratory Data Analysis and Visualization](#exploratory-data-analysis)
- [Conclusion](#conclusion)


## Project Overview

**FinSight** is a real-time financial portfolio analytics dashboard designed for investors and analysts to gain instant insights into asset performance. Built using Power BI, Python, and SQL Server, the system pulls and processes live market data, calculates investment returns, and visualizes profit/loss by asset class.


## Dataset Overview

- **Portfolio Table**: Stores user-purchased assets with quantity, purchase date, and type.
- **Market Data Table**: Pulls live prices using APIs like Alpha Vantage.
- **Assets Covered**: Stocks, Crypto, Mutual Funds, Commodities.
- **Fields**:  
  - asset_symbol, asset_type, buy_price, quantity, purchase_date  
  - current_price, timestamp


## Technologies Used

| Layer | Technology |
|-------|------------|
| Dashboard | Power BI |
| Scripting | Python (Requests, pyodbc) |
| Database | SQL Server |
| Calculations | DAX, Power Query |
| API Source | Alpha Vantage |


## Data Cleaning and Feature Engineering

- Removed unmatched or null asset entries
- Created derived metrics:
  - **Total Investment** = Quantity × Buy Price
  - **Current Value** = Quantity × Current Price
  - **Profit/Loss** = Current Value − Total Investment
- Joined portfolio with live market data via asset_symbol
- Filtered records by purchase date for time-based analysis

## Exploratory Data Analysis

### Visual Insights:
- **KPI Cards**: Total Investment, Current Value, Net Profit/Loss
- **Bar Chart**: Profit/Loss by Asset Symbol
- **Pie Chart**: Asset Allocation by Type
- **Table**: Asset-wise Performance with Conditional Formatting
- **Slicers**: Asset Type, Date Range Filters


## Conclusion

FinSight is a complete end-to-end portfolio analytics tool that blends **real-time data**, **SQL-backed architecture**, and **interactive dashboards** in Power BI. This project reflects strong skills in:
- Data engineering (ETL)
- Financial analytics
- Dashboard storytelling
