# Import libraries
import pandas as pd
import gdown
import plotly.express as px
import streamlit as st

# Load data from Google Drive
train_url = "https://drive.google.com/uc?id=1e9JI8ojE9JCwbp51fQ0XOxnYnBY0aw7T"
train_path = "train.csv"
gdown.download(train_url, train_path, quiet=False)

# Read the train dataset
train_df = pd.read_csv(train_path)

# Filter for churned customers
churned_customers = train_df[train_df['churn'] == 1]

# Streamlit setup
st.title("Customer Churn Analysis Dashboard")

# Visualizations

# 1. Age distribution of churned customers
st.subheader("Age Distribution of Churned Customers")
age_hist = px.histogram(churned_customers, x="age", nbins=20, title="Age Distribution")
st.plotly_chart(age_hist)

# 2. Churn by State
st.subheader("Churn by State")
state_bar = px.bar(churned_customers['state'].value_counts().reset_index(),
                   x='index', y='state', title="Churn by State", labels={'index': 'State', 'state': 'Churn Count'})
st.plotly_chart(state_bar)

# 3. Balance vs. Age (Scatter Plot)
st.subheader("Balance vs. Age for Churned Customers")
balance_age_scatter = px.scatter(churned_customers, x='age', y='balance', color='gender',
                                 title="Balance vs. Age (by Gender)")
st.plotly_chart(balance_age_scatter)

# 4. Tenure vs. Products (Heatmap)
st.subheader("Tenure vs. Number of Products for Churned Customers")
tenure_product_heatmap = px.density_heatmap(churned_customers, x='tenure', y='no_of_products',
                                            title="Tenure vs. Products")
st.plotly_chart(tenure_product_heatmap)

# 5. Credit Score Distribution
st.subheader("Credit Score Distribution of Churned Customers")
credit_hist = px.histogram(churned_customers, x='credit_score', nbins=20, title="Credit Score Distribution")
st.plotly_chart(credit_hist)

# 6. Churn by Gender
st.subheader("Churn by Gender")
gender_pie = px.pie(churned_customers, names='gender', title="Churn by Gender")
st.plotly_chart(gender_pie)
