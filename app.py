import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load data from Google Drive
import gdown

# Train dataset
train_url = "https://drive.google.com/uc?id=1e9JI8ojE9JCwbp51fQ0XOxnYnBY0aw7T"
train_path = "train.csv"
gdown.download(train_url, train_path, quiet=False)

# Sidebar filters
st.sidebar.title("Filters for Churn Analysis")
states = st.sidebar.multiselect("Select States:", options=train_df['state'].unique())
products = st.sidebar.multiselect("Select Number of Products:", options=train_df['no_of_products'].unique())
activity_status = st.sidebar.selectbox("Customer Active Status:", options=['All', 0, 1])

# Filter the data based on sidebar selections
filtered_df = train_df.copy()
if states:
    filtered_df = filtered_df[filtered_df['state'].isin(states)]
if products:
    filtered_df = filtered_df[filtered_df['no_of_products'].isin(products)]
if activity_status != 'All':
    filtered_df = filtered_df[filtered_df['active'] == int(activity_status)]

# Main title
st.title("Customer Churn Analysis Dashboard")

# 1. Credit Score Distribution by Churn Status
st.subheader("Credit Score Distribution by Churn Status")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=filtered_df, x='credit_score', hue='churn', kde=True, palette='viridis', bins=30, ax=ax)
st.pyplot(fig)

# 2. Age Distribution for Churned Customers
st.subheader("Age Distribution of Churned Customers")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_df[filtered_df['churn'] == 1]['age'], kde=True, color='salmon', ax=ax)
st.pyplot(fig)

# 3. Churn Rate by Number of Products
st.subheader("Churn Rate by Number of Products")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='no_of_products', hue='churn', data=filtered_df, palette='Set2', ax=ax)
st.pyplot(fig)

# 4. Balance Comparison for Churned vs. Retained Customers
st.subheader("Balance Comparison by Churn Status")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='churn', y='balance', data=filtered_df, palette='coolwarm', ax=ax)
st.pyplot(fig)

# 5. Churn Rate by State
st.subheader("Churn Rate by State")
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(x='state', hue='churn', data=filtered_df, palette='viridis', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# 6. Active vs. Inactive Customers and Churn Rate
st.subheader("Churn Rate by Customer Activity")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='active', hue='churn', data=filtered_df, palette='Set1', ax=ax)
st.pyplot(fig)

# 7. Estimated Salary Distribution for Churned Customers
st.subheader("Estimated Salary Distribution for Churned Customers")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_df[filtered_df['churn'] == 1]['estimated_salary'], kde=True, color='dodgerblue', ax=ax)
st.pyplot(fig)
