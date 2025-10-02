from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column
import pickle

# Load preprocessed data
with open("../Bokeh/monthly_avg.pkl", "rb") as f:
    avg_times = pickle.load(f)

# Get sorted list of months
months = sorted(avg_times["ALL"].keys())

# Default zipcodes
zip1 = list(avg_times.keys())[0]
zip2 = list(avg_times.keys())[1]

# Prepare data
def make_source(zip1, zip2):
    y_all = [avg_times["ALL"].get(m, 0) for m in months]
    y1 = [avg_times.get(zip1, {}).get(m, 0) for m in months]
    y2 = [avg_times.get(zip2, {}).get(m, 0) for m in months]
    return ColumnDataSource(data={"month": months, "ALL": y_all, "ZIP1": y1, "ZIP2": y2})

source = make_source(zip1, zip2)

# Create figure
p = figure(x_range=months, height=400, width=800, title="Monthly Avg Response Time (Hours)")
p.line(x='month', y='ALL', source=source, color="black", legend_label="ALL")
p.line(x='month', y='ZIP1', source=source, color="blue", legend_label="Zipcode 1")
p.line(x='month', y='ZIP2', source=source, color="red", legend_label="Zipcode 2")
p.xaxis.axis_label = "Month"
p.yaxis.axis_label = "Avg Response Time (Hours)"
p.legend.location = "top_left"

# Dropdowns for zipcodes
zipcodes = [z for z in avg_times.keys() if z != "ALL"]
select1 = Select(title="Zipcode 1", value=zip1, options=zipcodes)
select2 = Select(title="Zipcode 2", value=zip2, options=zipcodes)

# Callback
def update(attr, old, new):
    new_source = make_source(select1.value, select2.value)
    source.data.update(new_source.data)

select1.on_change("value", update)
select2.on_change("value", update)

# Layout
layout = column(select1, select2, p)
curdoc().add_root(layout)
curdoc().title = "311 Response Time Dashboard"
