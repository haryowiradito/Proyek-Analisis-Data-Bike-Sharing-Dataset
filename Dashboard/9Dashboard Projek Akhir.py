import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load clean data
all_df = pd.read_csv("all_data.csv")

# header
st.header('Bike Sharing Dashboard')

# amount of rental in seasons
st.subheader('Amount of Rental in Seasons')
byseason_df = all_df.groupby(by="season")["cnt"].sum().reset_index()
byseason_df.rename(columns={
    "cnt": "rental_count"
}, inplace=True)

fig, ax = plt.subplots(figsize=(20, 10))
 
sns.barplot(
    y="rental_count", 
    x="season",
    data=byseason_df.sort_values(by="rental_count", ascending=False),
    ax=ax
)
ax.set_title("Number of Rental in Seasons", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

# average rental of the day by hour
byhour_df = all_df.groupby('hr')['cnt'].mean()

st.subheader('Average Rental Traffic in Hour')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    byhour_df.index,
    byhour_df,
    marker='o', 
    linewidth=2,
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.caption('Copyright (c) Haryo Wiradito Bangkit 2024')