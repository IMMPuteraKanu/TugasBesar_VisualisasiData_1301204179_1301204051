import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/IMMPuteraKanu/Visdat/main/IndonesianSalary.csv")

# Set up Streamlit components
st.title('Dataset Visualization')
st.subheader('Select Options')
selected_area = st.selectbox("REGION", df['REGION'].unique())
start_year = st.slider("From", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].min())
end_year = st.slider("To", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].max())

# Filter the data
filtered_data = df[(df['REGION'] == selected_area) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

# Update the visualization
st.subheader('Data for {} - Year {} to {}'.format(selected_area, start_year, end_year))
st.line_chart(filtered_data[['YEAR', 'SALARY']])
