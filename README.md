# News Sentiment Analysis & Stock Return Correlation

**Turning Financial News into Alpha**  
*Week 1 Project - 10 Academy KAIM*

## Overview

This project analyzes the relationship between **financial news sentiment** and **stock price movements** for five major technology companies:  
**AAPL, AMZN, GOOG, META, and NVDA**.

The analysis is divided into three main tasks:
- **Task 1**: Exploratory Data Analysis (EDA) on the financial news dataset
- **Task 2**: Technical Indicators Analysis using TA-Lib
- **Task 3**: VADER Sentiment Analysis + Correlation with daily stock returns

---

## Project Structure

```bash
news-sentiment-analysis/
├── data/
│   └── raw/
│       ├── news.csv
│       └── stockData/
│           ├── AAPL.csv
│           ├── AMZN.csv
│           ├── GOOG.csv
│           ├── META.csv
│           └── NVDA.csv
│
├── notebooks/
│   ├── AAPL_analysis.ipynb
│   ├── AMZN_analysis.ipynb
│   ├── GOOG_analysis.ipynb
│   ├── META_analysis.ipynb
│   └── NVDA_analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── eda.py
│   ├── indicators.py          # TA-Lib functions
│   ├── sentiment.py           # VADER implementation
│   └── visualization.py
│
├── reports/
│   └── Final_Report_Week-1.pdf
│
├── requirements.txt
├── README.md
└── .gitignore