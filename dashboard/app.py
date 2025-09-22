import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Load Data ----------
@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\Getrude\Desktop\product-kpi-dashboard\Product-KPI-dashboard\data\product_data.csv", parse_dates=["date"])
    data["month"] = data["date"].dt.to_period("M").astype(str)
    return data

data = load_data()

# ---------- Dashboard Setup ----------
st.set_page_config(page_title="Product KPI Dashboard", layout="wide")
st.title("📊 Product KPI Dashboard")

# ---------- Filters ----------
date_range = st.date_input(
    "Select Date Range",
    [data["date"].min(), data["date"].max()]
)

mask = (data["date"] >= pd.to_datetime(date_range[0])) & (data["date"] <= pd.to_datetime(date_range[1]))
filtered = data.loc[mask]

# ---------- KPI Cards ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"${filtered['revenue'].sum():,.0f}")
col2.metric("👥 Avg Daily Active Users", f"{filtered['active_users'].mean():,.0f}")
col3.metric("🆕 Total New Users", f"{filtered['new_users'].sum():,.0f}")
col4.metric("📉 Avg Churn Rate", f"{filtered['churn_rate'].mean()*100:.2f}%")

# ---------- Charts ----------
# Revenue Trend
st.subheader("Revenue Over Time")
fig_rev = px.line(filtered, x="date", y="revenue", title="Revenue Trend")
st.plotly_chart(fig_rev, use_container_width=True)

# New Users Per Month
st.subheader("New Users Per Month")
monthly_users = filtered.groupby("month")["new_users"].sum().reset_index()
fig_users = px.bar(monthly_users, x="month", y="new_users", title="New Users Per Month")
st.plotly_chart(fig_users, use_container_width=True)

# Daily Active Users
st.subheader("Daily Active Users")
fig_dau = px.line(filtered, x="date", y="active_users", title="Daily Active Users")
st.plotly_chart(fig_dau, use_container_width=True)

# Churn Rate
st.subheader("Churn Rate Over Time")
fig_churn = px.area(filtered, x="date", y="churn_rate", title="Churn Rate (%)")
st.plotly_chart(fig_churn, use_container_width=True)

