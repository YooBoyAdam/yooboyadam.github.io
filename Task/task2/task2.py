import pandas as pd
import plotly.express as px

df = pd.read_csv('election_data.csv')

# Sort the data frame by 'year'
df = df.sort_values('year')

df['pct_absentee'] = df['absentee_ballots'] / df['TotalVoteTurnout'] * 100
df['pct_turnout'] = df['TotalVoteTurnout'] / df['ActiveRegisteredVoters'] * 100

# Put all region names in title case
df['region'] = df['region'].apply(lambda x: x.title())
df['Year'] = df['year']
df['Percentage Turnout'] = df['pct_turnout']
df['Percentage Absentee'] = df['pct_absentee']
fig = px.scatter(df,
                 x='pct_turnout',
                 y='pct_absentee',
                 size='ActiveRegisteredVoters',
                 color='region',
                 animation_frame='Year',  # Display 'Year' instead of 'year'
                 hover_name='locality',

                 hover_data={'pct_turnout': False,
                             'pct_absentee': False,
                             'year': False,
                             'region': False,
                             'Year': False,
                             'Percentage Turnout': ':.2f',
                             'Percentage Absentee': ':.2f',
                             'ActiveRegisteredVoters': ':.0f'},
                 color_discrete_sequence=px.colors.qualitative.Pastel,
                 title='Percentage Turnout vs. Percentage Absentee Ballots')

# Set legend title for 'region' in title case
fig.update_layout(legend_title=dict(text='Region', font=dict(size=20)))

fig.update_layout(title_x=0.5,
                  xaxis_title='Percentage Turnout',
                  yaxis_title='Percentage Absentee Ballots',
                  height=600,
                  width=800,
                  xaxis=dict(tickfont=dict(size=20), titlefont=dict(size=20)),
                  yaxis=dict(tickfont=dict(size=20), titlefont=dict(size=20)),
                  hoverlabel=dict(bgcolor='white'))

fig.update_traces(marker=dict(sizemode='diameter', sizeref=0.1))

# Fix jumping axes by setting x and y axes range manually
min_x, max_x = df['pct_turnout'].min(), df['pct_turnout'].max()
min_y, max_y = df['pct_absentee'].min(), df['pct_absentee'].max()
fig.update_xaxes(range=[min_x - 1, max_x + 1])
fig.update_yaxes(range=[min_y - 1, max_y + 1])

fig.write_html('bubble.html')

fig.show()
