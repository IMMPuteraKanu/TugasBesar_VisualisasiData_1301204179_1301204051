import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/IMMPuteraKanu/Visdat/main/IndonesianSalary.csv")

# Set up Streamlit components
st.title('Dataset Visualization')
st.subheader('Select Options')
selected_area1 = st.selectbox("Region 1", df['REGION'].unique())
selected_area2 = st.selectbox("Region 2", df['REGION'].unique())
start_year = st.slider("From", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].min())
end_year = st.slider("To", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].max())

# Filter the data for region 1
filtered_data1 = df[(df['REGION'] == selected_area1) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

# Filter the data for region 2
filtered_data2 = df[(df['REGION'] == selected_area2) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

# Update the visualization
st.subheader('Comparison of Data for {} and {} - Year {} to {}'.format(selected_area1, selected_area2, start_year, end_year))
st.line_chart(filtered_data1[['YEAR', 'SALARY']])
st.line_chart(filtered_data2[['YEAR', 'SALARY']])
