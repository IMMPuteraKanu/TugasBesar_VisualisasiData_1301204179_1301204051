import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.layouts import widgetbox, row, column
from bokeh.models import Select, Slider

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/IMMPuteraKanu/Visdat/main/IndonesianSalary.csv")

source = ColumnDataSource(data=df)

plot = figure(title='Dataset Visualization', x_axis_label='YEAR', y_axis_label='SALARY', plot_height=400, plot_width=600)
line = plot.line(x='YEAR', y='SALARY', source=source, line_width=2)


min_ = df['YEAR'].min()
max_= df['YEAR'].max()

select_region = st.Select(title="REGION", value=df['REGION'].unique()[0], options=df['REGION'].unique().tolist())

slider1 = Slider(title="From", start=min_, end=max_, value=min_, step=1)
slider2 = Slider(title="To", start=min_, end=max_, value=max_, step=1)

def update_plot(attr, old, new):
    selected_area = select_region.value
    start_year = slider1.value
    end_year = slider2.value

    # Memfilter data sesuai dengan area dan rentang tahun yang dipilih
    filtered_data = df[(df['REGION'] == selected_area) & (df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]

    # Memperbarui data pada ColumnDataSource plot line
    source.data = filtered_data

    # Memperbarui label pada sumbu x dan y plot line
    plot.xaxis.axis_label = 'Year'
    plot.yaxis.axis_label = 'Salary'

    # Memperbarui judul plot line
    plot.title.text = f"Data for {selected_area} - Year {start_year} to {end_year}"

select_region.on_change('value', update_plot)
slider1.on_change('value', update_plot)
slider2.on_change('value', update_plot)


layout = row(widgetbox(select_region, slider1, slider2), plot)
    
curdoc().add_root(layout)  
    
