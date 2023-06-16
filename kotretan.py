import pandas as pd
import streamlit as st
import altair as alt
import geopandas as gpd
import folium

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

# Combine the data for both regions
combined_data = pd.concat([filtered_data1, filtered_data2])

# Create the visualization
chart = alt.Chart(combined_data).mark_line().encode(
    x='YEAR',
    y='SALARY',
    color='REGION'
).properties(
    width=600,
    height=400,
    title='Comparison of Data for {} and {} - Year {} to {}'.format(selected_area1, selected_area2, start_year, end_year)
)

# Grafik
st.altair_chart(chart)

# Filter the shapefile for the selected regions
filtered_gdf = gdf[gdf['REGION'].isin([selected_area1, selected_area2])]

# Create a folium map
m = folium.Map(location=[-2, 118], zoom_start=5)

# Add the shapefile to the map
folium.GeoJson(filtered_gdf).add_to(m)

# Display the map
st.subheader('Selected Regions on Map:')
st.write(m._repr_html_(), unsafe_allow_html=True)
