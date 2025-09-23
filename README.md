# 📊 Product KPI Dashboard

## 📌 Project Overview
The **Product KPI Dashboard** is an interactive analytics tool built with **Streamlit, Pandas, and Plotly**.  
It enables product teams and decision-makers to monitor performance, track growth, and identify risks using key metrics such as **Revenue, Daily Active Users (DAU), New Users, and Churn Rate**.

This dashboard is designed to give both a **high-level overview** and **detailed insights** into product health.

---

## 🎯 Key Metrics Tracked

- **💰 Revenue**  
  Total sales generated over time. This helps evaluate financial growth and the overall success of the product.

- **👥 Daily Active Users (DAU)**  
  The number of unique users interacting with the product daily. DAU is a strong measure of engagement and product stickiness.

- **🆕 New Users**  
  The count of users who signed up in a given period. This tracks acquisition and marketing effectiveness.

- **📉 Churn Rate**  
  The percentage of users who stop using the product. A critical measure for retention and long-term sustainability.

---

## 📸 Dashboard Screenshots

### 1. Full Dashboard
Overview of the KPI dashboard combining all metrics in one place.  
![Dashboard Overview](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/dashboard.png)

### 2. Revenue Trend
Line chart showing total revenue growth over time.  
![Revenue Trend](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/Revenue%20trend%20.png)

### 3. New Users
Bar chart showing new user signups per month.  
![New Users](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/New%20users%20per%20month.png)

### 4. Churn Rate
Area chart highlighting the percentage of users leaving the product.  
![Churn Rate](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/churn%20rate.png)

---

## 🗂️ Project Structure

```
product-kpi-dashboard/
│
├── data/                # datasets (simulated or real)
│   └── product_data.csv
│
├── dashboard/           # Streamlit app
│   └── app.py
│
├── docs/                # documentation & screenshots
│   └── dashboard_preview.png
│
├── notebooks/           # Jupyter notebooks (EDA, KPI calculations)
│   └── data_exploration.ipynb
│
├── scripts/             # utility scripts (data generation, ETL)
│   └── generate_data.py
│
├── requirements.txt     # dependencies
└── README.md            # project overview
```


