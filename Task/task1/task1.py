import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

data = pd.read_csv("vote_subset.csv")

# Convert voter_cat values to title case
data['voter_cat'] = data['voter_cat'].str.title()

color_mapping = {'Always': 'darkgreen', 'Sporadic': 'darkorange', 'Rarely/Never': 'lightgray'}
data['color'] = data['voter_cat'].map(color_mapping).astype('category').cat.codes

# Specify the desired order for income categories
income_order = ['$125k or more', '$75-125k', '$40-75k', 'Less than $40k']
data['income_cat'] = pd.Categorical(data['income_cat'], categories=income_order, ordered=True)

fig = go.Figure(go.Parcats(
    dimensions=[
        {'label': 'Voter Category', 'values': data['voter_cat']},
        {'label': 'Education', 'values': data['education']},
        {'label': 'Income Category', 'values': data['income_cat']}
    ],
    counts=data.index,
    line={'color': data['color'], 'colorscale': [[0, 'darkgreen'], [0.5, 'darkorange'], [1, 'lightgray']]},
    hoverinfo='count',
    hoveron='color',
    labelfont=dict(size=14),
    tickfont=dict(size=12)
))

fig.update_layout(
    title='Parallel Categories Plot of Voter Frequency, Education, and Income',
    width=800,
    height=600,
    font=dict(size=14)
)


fig.write_html('categories.html')
fig.show()
