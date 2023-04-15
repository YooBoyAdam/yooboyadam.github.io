import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

data = pd.read_csv("vote_subset.csv")


color_mapping = {'always': 'darkgreen', 'sporadic': 'darkorange', 'rarely/never': 'lightgray'}
data['color'] = data['voter_cat'].map(color_mapping)

fig = px.parallel_categories(
    data,
    dimensions=['voter_cat', 'education', 'income_cat'],
    labels={'voter_cat': 'Voter Category', 'education': 'Education', 'income_cat': 'Income Catagory'},
    color='color',
    color_continuous_scale=['darkgreen', 'darkorange', 'lightgray'],
    title="Parallel Categories Plot of Voter Frequency, Education, and Income"
)

fig.update_layout(
    title='Parallel Categories Plot of Voter Frequency, Education, and Income',
    width=800,
    height=600,
    font=dict(size=14)
)

fig.update_traces(
    line=dict(colorscale=[[0, 'darkgreen'], [1, 'darkorange']]),
    selector=dict(type='parcats'),
    hovertemplate='%{count} <%{hovertext}'
)

fig.write_html('categories.html')
fig.show()
