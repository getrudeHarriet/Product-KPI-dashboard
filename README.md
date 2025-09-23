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
This dashboard brings together all KPIs — revenue, user growth, daily engagement, and churn — into one view.  
It provides a **snapshot of overall product performance**, allowing teams to track financial health, customer acquisition, engagement, and retention simultaneously.  
This helps product managers and stakeholders **quickly identify growth patterns and potential risks**. 
![Dashboard Overview](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/dashboard.png)

### 2. Revenue Trend
The revenue trend chart shows how sales have evolved over time.  
From the visualization, stakeholders can assess whether the product is achieving **steady financial growth** or facing dips that might require deeper investigation.  
It enables the business to connect revenue changes to **campaigns, feature launches, or seasonality**, helping guide **strategic decisions** on pricing, promotions, or investments.  
![Revenue Trend](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/Revenue%20trend%20.png)

### 3. New Users
This chart tracks the number of new users joining each month.  
It reveals the effectiveness of **marketing campaigns, referrals, or product visibility**.  
If the chart shows a strong upward trend, it signals **successful acquisition strategies**, while a decline would highlight the need to revisit **customer acquisition channels**. 
![New Users](https://github.com/getrudeHarriet/Product-KPI-dashboard/blob/main/docs/New%20users%20per%20month.png)

### 4. Churn Rate
The churn chart measures the percentage of users leaving the product over time.  
It provides insight into **customer satisfaction and retention**.  
High churn means new customers are not staying, which can **cancel out growth gains**, while stable or declining churn suggests the product is **retaining value** for users.  
This is critical for evaluating whether growth is **sustainable long-term**. 
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


