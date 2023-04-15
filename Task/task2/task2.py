import pandas as pd
import plotly.express as px



df = pd.read_csv('election_data.csv')

df['pct_absentee'] = df['absentee_ballots'] / df['TotalVoteTurnout'] * 100
df['pct_turnout'] = df['TotalVoteTurnout'] / df['ActiveRegisteredVoters'] * 100


fig = px.scatter(df,
                 x='pct_turnout',
                 y='pct_absentee',
                 size='ActiveRegisteredVoters',
                 color='region',
                 animation_frame='year',
                 hover_name='locality',
                 hover_data={'pct_turnout': ':.2f',
                             'pct_absentee': ':.2f',
                             'ActiveRegisteredVoters': ':.0f'},
                 color_discrete_sequence=px.colors.qualitative.Pastel,
                 title='Percentage Turnout vs. Percentage Absentee Ballots')

fig.update_layout(title_x=0.5,
                  xaxis_title='Percentage Turnout',
                  yaxis_title='Percentage Absentee Ballots',
                  height=600,
                  width=800,
                  xaxis=dict(tickfont=dict(size=20), titlefont=dict(size=20)),
                  yaxis=dict(tickfont=dict(size=20), titlefont=dict(size=20)),
                  hoverlabel=dict(bgcolor='white'))

fig.update_traces(marker=dict(sizemode='diameter', sizeref=0.1))


##fig.write_image('bubble.png')
fig.write_html('bubble.html')


fig.show()
