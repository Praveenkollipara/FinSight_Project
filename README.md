# FinSight_Project


## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Overview](#dataset-overview)
- [Technologies Used](#technologies-used)
- [Data Cleaning and Feature Engineering](#data-cleaning-and-feature-engineering)
- [Exploratory Data Analysis and Visualization](#exploratory-data-analysis-and-visualization)
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
