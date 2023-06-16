import pandas as pd
import streamlit as st
import altair as alt

# Dataset Indonesia Salary
df = pd.read_csv("https://raw.githubusercontent.com/IMMPuteraKanu/Visdat/main/IndonesianSalary.csv")

# Membuat Button Dengan Streamit
st.title('Dataset Visualization 1301204179 - ')
st.subheader('Select Options')
selected_area1 = st.selectbox("Region 1", df['REGION'].unique())
selected_area2 = st.selectbox("Region 2", df['REGION'].unique())
start_year = st.slider("From", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].min())
end_year = st.slider("To", min_value=df['YEAR'].min(), max_value=df['YEAR'].max(), value=df['YEAR'].max())

# Filter Data Region 1
filtered_data1 = df[(df['REGION'] == selected_area1) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

# Filter Data Region 2
filtered_data2 = df[(df['REGION'] == selected_area2) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

# Menggabungkan 2 Data Region
combined_data = pd.concat([filtered_data1, filtered_data2])

# Menghitung Selisih Rata - Rata 2 Daerah
average_diff = filtered_data1['SALARY'].mean() - filtered_data2['SALARY'].mean()

# Menghitung Selisih Nilai Max dan Min 2 Daerah
max_diff = combined_data['SALARY'].max() - combined_data['SALARY'].min()
min_diff = combined_data['SALARY'].min() - combined_data['SALARY'].max()

# Membuat Visualisasi
chart = alt.Chart(combined_data).mark_line().encode(
    x='YEAR',
    y='SALARY',
    color='REGION',
    tooltip=['YEAR', 'SALARY']
).properties(
    width=600,
    height=400,
    title='Comparison of Data for {} and {} - Year {} to {}'.format(selected_area1, selected_area2, start_year, end_year)
)

# Display Grafik
st.altair_chart(chart)

# Display Rata - Rata Selisih 2 Daerah
st.subheader('Average Salary Difference:')
st.write("The average salary difference between {} and {} is: {:.2f}".format(selected_area1, selected_area2, average_diff))

# Display Selisih Max dan Min 2 Daerah
st.subheader('Maximum and Minimum Salary Differences:')
st.write("The maximum salary difference between {} and {} is: {:.2f}".format(selected_area1, selected_area2, max_diff))
st.write("The minimum salary difference between {} and {} is: {:.2f}".format(selected_area1, selected_area2, min_diff))
